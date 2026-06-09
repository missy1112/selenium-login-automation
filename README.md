# Selenium Login Automation

This is a beginner-friendly QA automation project built with Selenium and Pytest.  
The project tests login functionality on a demo website using automated browser testing.

## Project Objective

The goal of this project is to practice web automation testing by checking common login scenarios, including successful login, invalid login, and logout functionality.

## Website Tested

https://the-internet.herokuapp.com/login

## Tools Used

- Python
- Selenium
- Pytest
- WebDriver Manager
- Git
- GitHub
- Visual Studio Code

## Test Scenarios Covered

| Test Case | Description | Status |
|---|---|---|
| Valid Login | Checks that a user can log in with correct credentials | Passed |
| Invalid Login | Checks that an error message appears for incorrect credentials | Passed |
| Logout | Checks that a logged-in user can log out successfully | Passed |

## Project Structure

```text
selenium-login-automation/
├── screenshots/
├── tests/
│   └── test_login.py
├── .gitignore
├── README.md
└── requirements.txt