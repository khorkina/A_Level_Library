import os
from flask import Flask, render_template, send_from_directory
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key")

# Subject configuration
SUBJECTS = {
    'business': {
        'name': 'Business A-Level',
        'description': 'Comprehensive business studies materials'
    },
    'psychology': {
        'name': 'Psychology A-Level',
        'description': 'In-depth psychology resources'
    },
    'sociology': {
        'name': 'Sociology A-Level',
        'description': 'Essential sociology study materials'
    },
    'english': {
        'name': 'English A-Level',
        'description': 'Literature and language resources'
    }
}

@app.route('/')
def index():
    return render_template('index.html', subjects=SUBJECTS)

@app.route('/subject/<subject_name>')
def subject(subject_name):
    if subject_name not in SUBJECTS:
        return "Subject not found", 404
    
    # In production, this would scan a real directory
    # For now, we'll use sample PDF data
    pdfs = [
        {'name': f'Chapter 1 - Introduction to {subject_name.title()}', 'filename': 'chapter1.pdf'},
        {'name': f'Chapter 2 - Advanced {subject_name.title()} Concepts', 'filename': 'chapter2.pdf'},
        {'name': f'Practice Papers - {subject_name.title()}', 'filename': 'practice.pdf'}
    ]
    
    return render_template('subject.html', 
                         subject=SUBJECTS[subject_name],
                         subject_name=subject_name,
                         pdfs=pdfs)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('vip_folder', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
