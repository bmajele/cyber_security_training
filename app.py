from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from sqlalchemy import func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cybersecurity.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_hr = db.Column(db.Boolean, default=False)
    test_results = db.relationship('TestResult', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    correct_answer = db.Column(db.String(500), nullable=False)
    options = db.Column(db.String(1000), nullable=False)  # Store as comma-separated values

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_taken = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_hr:
        return redirect(url_for('hr_dashboard'))
    
    # Get user's test results
    results = TestResult.query.filter_by(user_id=current_user.id).order_by(TestResult.date_taken).all()
    
    # Prepare data for score trend graph
    score_data = {
        'labels': [result.date_taken.strftime('%Y-%m-%d %H:%M') for result in results],
        'scores': [result.score for result in results]
    }
    
    return render_template('dashboard.html', score_data=score_data)

@app.route('/take_test')
@login_required
def take_test():
    if current_user.is_hr:
        return redirect(url_for('hr_dashboard'))
    questions = Question.query.all()
    return render_template('test.html', questions=questions)

@app.route('/submit_test', methods=['POST'])
@login_required
def submit_test():
    if current_user.is_hr:
        return redirect(url_for('hr_dashboard'))
    
    score = 0
    questions = Question.query.all()
    
    for question in questions:
        user_answer = request.form.get(f'question_{question.id}')
        if user_answer == question.correct_answer:
            score += 1
    
    test_result = TestResult(user_id=current_user.id, score=score)
    db.session.add(test_result)
    db.session.commit()
    
    return redirect(url_for('results'))

@app.route('/results')
@login_required
def results():
    if current_user.is_hr:
        return redirect(url_for('hr_dashboard'))
    results = TestResult.query.filter_by(user_id=current_user.id).all()
    return render_template('results.html', results=results)

@app.route('/hr_dashboard')
@login_required
def hr_dashboard():
    if not current_user.is_hr:
        return redirect(url_for('dashboard'))
    
    # Get all test results
    results = TestResult.query.join(User).all()
    
    # Get all unique users who have taken tests
    users = User.query.join(TestResult).distinct().all()
    
    # Calculate average scores per day for the last 30 days
    thirty_days_ago = datetime.now() - timedelta(days=30)
    daily_averages = db.session.query(
        func.date(TestResult.date_taken).label('date'),
        func.avg(TestResult.score).label('average_score')
    ).filter(TestResult.date_taken >= thirty_days_ago).group_by(
        func.date(TestResult.date_taken)
    ).order_by(func.date(TestResult.date_taken)).all()

    # Get user performance distribution
    score_distribution = db.session.query(
        TestResult.score,
        func.count(TestResult.id).label('count')
    ).group_by(TestResult.score).all()
    
    # Get user-specific performance data
    user_performance = {}
    for user in users:
        user_results = TestResult.query.filter_by(user_id=user.id).order_by(TestResult.date_taken).all()
        user_performance[user.email] = {
            'labels': [result.date_taken.strftime('%Y-%m-%d %H:%M') for result in user_results],
            'scores': [result.score for result in user_results],
            'average': sum(result.score for result in user_results) / len(user_results) if user_results else 0,
            'total_tests': len(user_results)
        }
    
    # Prepare data for graphs
    trend_data = {
        'labels': [str(avg.date) for avg in daily_averages],
        'averages': [float(avg.average_score) for avg in daily_averages]
    }
    
    distribution_data = {
        'scores': [d.score for d in score_distribution],
        'counts': [d.count for d in score_distribution]
    }
    
    return render_template('hr_dashboard.html', 
                         results=results,
                         trend_data=trend_data,
                         distribution_data=distribution_data,
                         user_performance=user_performance)

@app.route('/manage_questions')
@login_required
def manage_questions():
    if not current_user.is_hr:
        return redirect(url_for('dashboard'))
    questions = Question.query.all()
    return render_template('manage_questions.html', questions=questions)

@app.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question():
    if not current_user.is_hr:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        question_text = request.form.get('question_text')
        correct_answer = request.form.get('correct_answer')
        options = request.form.getlist('options[]')
        
        # Filter out empty options and join with commas
        options = [opt for opt in options if opt.strip()]
        if correct_answer not in options:
            options.append(correct_answer)
        options_str = ','.join(options)
        
        question = Question(
            question_text=question_text,
            correct_answer=correct_answer,
            options=options_str
        )
        db.session.add(question)
        db.session.commit()
        flash('Question added successfully!')
        return redirect(url_for('manage_questions'))
    
    return render_template('add_question.html')

@app.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
@login_required
def edit_question(question_id):
    if not current_user.is_hr:
        return redirect(url_for('dashboard'))
    
    question = Question.query.get_or_404(question_id)
    
    if request.method == 'POST':
        question.question_text = request.form.get('question_text')
        question.correct_answer = request.form.get('correct_answer')
        options = request.form.getlist('options[]')
        
        # Filter out empty options and join with commas
        options = [opt for opt in options if opt.strip()]
        if question.correct_answer not in options:
            options.append(question.correct_answer)
        question.options = ','.join(options)
        
        db.session.commit()
        flash('Question updated successfully!')
        return redirect(url_for('manage_questions'))
    
    return render_template('edit_question.html', question=question)

@app.route('/delete_question/<int:question_id>', methods=['POST'])
@login_required
def delete_question(question_id):
    if not current_user.is_hr:
        return redirect(url_for('dashboard'))
    
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully!')
    return redirect(url_for('manage_questions'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
