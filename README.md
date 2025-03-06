# A_Level_Library

A digital library for A-Level study materials across Business, Psychology, Sociology, and English subjects.

## Local Setup Instructions

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Clone the Project
```sh
git clone <repository-url>
cd <project-directory>
```

### Create Required Directories
```sh
mkdir vip_folder
```

### Setup PDF Materials
Create the following structure in the `vip_folder` directory:
```
vip_folder/
├── Business_Materials/
├── English_Materials/
├── Psyhology_Materials/
└── Sociology_Materials/
```
Copy your PDF files into these directories maintaining the original folder structure:
- Business materials go into `vip_folder/Business_Materials/`
- Psychology materials go into `vip_folder/Psyhology_Materials/`
- Sociology materials go into `vip_folder/Sociology_Materials/`
- English materials go into `vip_folder/English_Materials/`

### Install Dependencies
```sh
pip install flask flask-sqlalchemy gunicorn email-validator psycopg2-binary
```

### Running the Application
```sh
python main.py
```
The application will be available at [http://localhost:5000](http://localhost:5000)

## Troubleshooting PDF Display
If PDFs are not displaying:

### Check File Permissions
- Ensure the PDF files have read permissions
- The application user must have access to the `vip_folder` directory

### Verify File Structure
- Confirm PDFs are in the correct subject folders under `vip_folder`
- Check that file paths match the expected structure

### Debug Mode
- The application runs in debug mode by default
- Check the console for any file access errors
- Verify the URLs being generated for PDF files

## Features
- Organized PDF materials by subject
- Intuitive navigation with category filters
- PDF preview functionality
- Responsive design for all devices
- Automatic sorting of materials by unit numbers (e.g., 4.1, 4.2, 4.3)

## Notes
- Make sure all PDF files are properly organized in their respective subject folders
- The application expects PDF files to be named with numerical prefixes (e.g., "1.1", "2.3") for proper sorting
- Keep the original folder structure within subject directories for proper categorization

