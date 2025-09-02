# Study Tool Application

## Overview
The Study Tool Application is a web-based platform designed to help users track their study progress across various subjects. It features user authentication, a dashboard for monitoring progress, and dedicated modules for subjects including math, English, biology, accounting, physics, chemistry, literature, economics, civic education, government, geography, and design.

## Features
- **User Authentication**: Secure login and registration for users.
- **Dashboard**: A personalized dashboard to track study progress and achievements.
- **Subject Modules**: Comprehensive resources and topics for each subject.

## Project Structure
```
study-tool-app
├── backend
│   ├── app.py
│   ├── auth
│   │   └── routes.py
│   ├── dashboard
│   │   └── routes.py
│   ├── modules
│   │   ├── math.py
│   │   ├── english.py
│   │   ├── biology.py
│   │   ├── accounting.py
│   │   ├── physics.py
│   │   ├── chemistry.py
│   │   ├── literature.py
│   │   ├── economics.py
│   │   ├── civic_education.py
│   │   ├── government.py
│   │   ├── geography.py
│   │   └── design.py
│   ├── models
│   │   └── user.py
│   ├── database
│   │   └── schema.sql
│   └── requirements.txt
├── frontend
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── subjects
│   │   ├── math.html
│   │   ├── english.html
│   │   ├── biology.html
│   │   ├── accounting.html
│   │   ├── physics.html
│   │   ├── chemistry.html
│   │   ├── literature.html
│   │   ├── economics.html
│   │   ├── civic_education.html
│   │   ├── government.html
│   │   ├── geography.html
│   │   └── design.html
│   ├── css
│   │   └── styles.css
│   └── js
│       ├── main.js
│       ├── auth.js
│       ├── dashboard.js
│       └── subjects.js
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the backend directory and install the required packages:
   ```
   cd backend
   pip install -r requirements.txt
   ```
3. Set up the database by running the schema:
   ```
   sqlite3 database/schema.sql
   ```
4. Start the backend server:
   ```
   python app.py
   ```
5. Open the frontend files in a web browser to access the application.

## Usage
- Register a new account or log in to an existing account.
- Access the dashboard to view your study progress.
- Explore different subject modules for resources and topics.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.