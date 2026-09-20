# QA Test Automation

A small web application testing project built to demonstrate **UI testing, API testing, database testing, and automated test execution** using Python.

## Project Overview

This project contains a simple Flask-based Login and Registration web application along with an automated testing framework.
The application is tested using **Selenium and Pytest** for UI testing, **Requests and Pytest** for API testing, and **SQLite** for database validation.
The project currently contains **18 automated test cases**, covering positive scenarios, negative scenarios, form validation, API responses, and database integrity.

## Features
### Web Application

- User Login
- User Registration
- Invalid login handling
- Duplicate email validation
- Form validation
- SQLite database storage

### Automated Testing
#### UI Testing — Selenium + Pytest

10 test cases covering:

- Successful login
- Invalid password
- Invalid email
- Empty email
- Empty password
- Successful registration
- Duplicate email
- Empty name
- Empty registration email
- Empty registration password

#### API Testing — Requests + Pytest
4 test cases covering:
- Login page response
- Registration page response
- Home page redirect
- Invalid URL / 404 response

#### Database Testing — SQLite
4 test cases covering:
- Users table existence
- Required database columns
- Test user verification
- Email uniqueness

## Test Results
```text
Total Tests: 18
Passed: 18
Failed: 0

Result: 18/18 Passed
```

## Tech Stack
- Python
- Flask
- Selenium
- Pytest
- Requests
- SQLite
- HTML
- CSS
- Git
- GitHub

## Project Structure
```text
QA-Test-Automation/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
├── templates/
│   ├── login.html
│   └── register.html
│
└── tests/
    ├── test_login.py
    ├── test_api.py
    └── test_database.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/harichandana-tech/QA-Test-Automation.git
```

Move into the project directory:

```bash
cd QA-Test-Automation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## Run Automated Tests

Keep the Flask application running and open another terminal.

Run all tests:
```bash
python -m pytest tests/ -v
```

Run UI tests:
```bash
python -m pytest tests/test_login.py -v
```

Run API tests:
```bash
python -m pytest tests/test_api.py -v
```

Run database tests:
```bash
python -m pytest tests/test_database.py -v
```

## Generate HTML Test Report

Install the HTML reporting plugin:
```bash
pip install pytest-html
```

Generate the test report:
```bash
python -m pytest tests/ -v --html=reports/test_report.html --self-contained-html
```

The generated report provides a summary of the automated test execution and individual test results.

## QA Concepts Demonstrated

- Functional Testing
- Positive Testing
- Negative Testing
- UI Automation
- API Testing
- Database Testing
- Test Case Design
- Assertions
- Form Validation Testing
- Data Integrity Testing
- Automated Test Execution
- Test Reporting
- Git & GitHub

## Author
**Hari Chandana**

GitHub: https://github.com/harichandana-tech
