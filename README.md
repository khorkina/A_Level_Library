# A_Level_Library

A-Level Educational Resource Library
A digital library for A-Level study materials across Business, Psychology, Sociology, and English subjects.

Local Setup Instructions
Prerequisites

Python 3.11 or higher
pip (Python package manager)
Clone the Project

Download all the project files to your local machine
Make sure to include the exam materials in a folder named vip_folder at the root of the project
Install Dependencies

pip install flask flask-sqlalchemy gunicorn email-validator psycopg2-binary
Project Structure Ensure your project structure looks like this:

your-project/
├── vip_folder/
│   ├── Business_Materials/
│   ├── English_Materials/
│   ├── Psyhology_Materials/
│   └── Sociology_Materials/
├── static/
│   ├── css/
│   └── js/
├── templates/
├── app.py
└── main.py
Running the Application

python main.py
The application will be available at http://localhost:5000

Features
Organized PDF materials by subject
Intuitive navigation with category filters
PDF preview functionality
Responsive design for all devices
Notes
The application is configured to run in debug mode by default
Make sure all PDF files are properly organized in their respective subject folders
The application expects PDF files to be named with numerical prefixes (e.g., "1.1", "2.3") for proper sorting
