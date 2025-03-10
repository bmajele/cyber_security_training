# Cyber Security Training Platform

A comprehensive web-based platform for conducting cyber security training and assessments, featuring First Alliance Bank's professional color scheme. The platform enables organizations to assess and track employee cybersecurity knowledge effectively.

## 🔑 Key Features

- **User Authentication System**
  - Role-based access (regular users and HR admins)
  - Secure password hashing
  - User registration and login

- **Cyber Security Testing**
  - Multiple-choice test format
  - Dynamic question management
  - Score tracking and result storage

- **Analytics Dashboard**
  - User dashboard with personal test history graph
  - HR dashboard with comprehensive analytics
  - Performance visualization using Chart.js
  - Score distribution charts
  - Individual user performance tracking

- **Question Management (HR Admin)**
  - Add new security questions
  - Edit existing questions
  - Delete questions
  - Dynamic option management

## 🎨 Design Features
- Professional First Alliance Bank color scheme
  - Primary Red: #C41E3A
  - Gold Accent: #FFB81C
- Responsive Bootstrap design
- Interactive data visualizations
- Modern UI/UX elements

## 🛠️ Technical Stack
- Backend: Python, Flask
- Database: SQLAlchemy with SQLite
- Frontend: HTML, Bootstrap, Chart.js
- Authentication: Flask-Login
- Form Handling: Flask-WTF

## 📦 Setup Instructions

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Initialize the database and create sample questions:
```bash
python init_db.py
```

3. Run the application:
```bash
python app.py
```

4. Access the application at `http://localhost:5000`

## 👤 Default Admin Account

- Email: admin@cybersec.com
- Password: AdminPass123!

## 🔒 Security Features
- Password hashing
- Role-based access control
- Protected routes for HR administrators
- Input validation
- Secure session management

## 📊 Analytics Features
- Individual performance tracking
- Overall test score trends
- Score distribution visualization
- Detailed results table with filtering
- User-specific performance graphs

## 🚀 Future Enhancements
- Password complexity requirements
- User profile management
- Enhanced test generation logic
- More granular access controls
- Certificate generation system

## 📝 Contributing
Feel free to fork this repository and submit pull requests for any enhancements.

## 📄 License
This project is licensed under the MIT License.
