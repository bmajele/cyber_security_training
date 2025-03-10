from app import app, db, User, Question, TestResult

def init_db():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create tables
        db.create_all()

        # Create admin user with HR privileges
        admin_user = User(email='admin@cybersec.com', is_hr=True)
        admin_user.set_password('AdminPass123!')
        db.session.add(admin_user)

        # Create sample questions
        questions = [
            {
                'question_text': 'What is phishing?',
                'options': 'A fraudulent attempt to obtain sensitive information,A type of fish,A computer virus,A networking protocol',
                'correct_answer': 'A fraudulent attempt to obtain sensitive information'
            },
            {
                'question_text': 'What is a strong password?',
                'options': '123456,password123,MyP@ssw0rd2023!,qwerty',
                'correct_answer': 'MyP@ssw0rd2023!'
            },
            {
                'question_text': 'What is two-factor authentication?',
                'options': 'Using two passwords,Using two different browsers,A security process requiring two forms of identification,Logging in twice',
                'correct_answer': 'A security process requiring two forms of identification'
            },
            {
                'question_text': 'What should you do if you suspect a security breach?',
                'options': 'Ignore it,Report it immediately to IT security,Wait and see what happens,Turn off your computer',
                'correct_answer': 'Report it immediately to IT security'
            },
            {
                'question_text': 'Which of these is a secure way to store passwords?',
                'options': 'In a text file on desktop,Using a password manager,Written on a sticky note,In an email draft',
                'correct_answer': 'Using a password manager'
            }
        ]

        # Add questions to database
        for q in questions:
            question = Question(
                question_text=q['question_text'],
                options=q['options'],
                correct_answer=q['correct_answer']
            )
            db.session.add(question)

        # Create HR user
        hr_user = User(email='hr@company.com', is_hr=True)
        hr_user.set_password('hr_password')
        db.session.add(hr_user)

        db.session.commit()

if __name__ == '__main__':
    init_db()
