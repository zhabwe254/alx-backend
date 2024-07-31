#i18n Project

This project demonstrates the implementation of internationalization (i18n) in a Flask application using Flask-Babel.

## Project Description

This project is a series of tasks that build upon each other to create a Flask application with internationalization features. It covers:

1. Setting up a basic Flask app
2. Integrating Flask-Babel for i18n
3. Implementing locale selection based on user preferences
4. Parametrizing templates for translation
5. Forcing locale selection via URL parameters
6. Mocking user login and using user preferences for locale
7. Implementing timezone selection

## Requirements

- Python 3.7
- Flask
- Flask-Babel
- pytz

All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.

## Installation

1. Clone this repository
2. Install the required packages:
pip install flask flask-babel pytz
Copy
## Usage

Each task is implemented in a separate Python file, numbered from 0 to 7. To run a specific task, use:
python3 <task-number>-app.py
Copy
For example, to run the first task:
python3 0-app.py
Copy
## File Descriptions

- `0-app.py`: Basic Flask app
- `1-app.py`: Basic Babel setup
- `2-app.py`: Get locale from request
- `3-app.py`: Parametrize templates
- `4-app.py`: Force locale with URL parameter
- `5-app.py`: Mock logging in
- `6-app.py`: Use user locale
- `7-app.py`: Infer appropriate time zone
- `templates/`: Directory containing HTML templates
- `translations/`: Directory containing translation files
- `babel.cfg`: Babel configuration file

## Author
GIDEON HABWE
