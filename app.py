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
        'description': 'Comprehensive business studies materials',
        'folder': 'Business_Materials',
        'categories': ['Unit 1 - Business Environment', 'Unit 2 - People', 'Unit 3 - Marketing',
                      'Unit 4 - Operations', 'Unit 5 - Finance', 'Unit 6 - Strategic Management',
                      'Responses', 'Additional Materials']
    },
    'psychology': {
        'name': 'Psychology A-Level',
        'description': 'In-depth psychology resources',
        'folder': 'Psyhology_Materials',  # Keeping original spelling from zip file
        'categories': ['Clinical', 'Consumer']
    },
    'sociology': {
        'name': 'Sociology A-Level',
        'description': 'Essential sociology study materials',
        'folder': 'Sociology_Materials',
        'categories': ['Education', 'Globalisation', 'Media']
    },
    'english': {
        'name': 'English A-Level',
        'description': 'Literature and language resources',
        'folder': 'English_Materials',
        'categories': ['Cheat Sheet', 'Examples', 'Guide']
    }
}

def detect_category(file_path, subject):
    path_parts = file_path.split(os.sep)

    # Map folder names to categories
    category_mapping = {
        'UNIT (1)': 'Unit 1 - Business Environment',
        'UNIT (2)': 'Unit 2 - People',
        'UNIT (3)': 'Unit 3 - Marketing',
        'UNIT (4)': 'Unit 4 - Operations',
        'UNIT (5)': 'Unit 5 - Finance',
        'UNIT (6)': 'Unit 6 - Strategic Management',
        'Responses': 'Responses',
        'Clinical': 'Clinical',
        'Consumer': 'Consumer',
        'Education': 'Education',
        'Globalisation': 'Globalisation',
        'Media': 'Media',
        'Cheat_Sheet': 'Cheat Sheet',
        'Examples': 'Examples',
        'Guide': 'Guide'
    }

    # Look for category in path
    for part in path_parts:
        for folder_name, category in category_mapping.items():
            if folder_name in part:
                return category

    return 'Additional Materials'

def get_pdfs_for_subject(subject_folder):
    pdfs = []
    base_path = os.path.join('vip_folder', subject_folder)

    if not os.path.exists(base_path):
        return pdfs

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.pdf'):
                # Create relative path from vip_folder
                rel_path = os.path.relpath(os.path.join(root, file), 'vip_folder')
                # Get a clean name by removing extension and replacing underscores
                name = os.path.splitext(file)[0].replace('_', ' ')

                # Detect category based on file path
                category = detect_category(rel_path, subject_folder)

                pdfs.append({
                    'name': name,
                    'filename': rel_path,
                    'category': category
                })
    return sorted(pdfs, key=lambda x: (x['category'], x['name']))

@app.route('/')
def index():
    return render_template('index.html', subjects=SUBJECTS)

@app.route('/subject/<subject_name>')
def subject(subject_name):
    if subject_name not in SUBJECTS:
        return "Subject not found", 404

    subject_info = SUBJECTS[subject_name]
    pdfs = get_pdfs_for_subject(subject_info['folder'])

    return render_template('subject.html', 
                         subject=subject_info,
                         subject_name=subject_name,
                         pdfs=pdfs,
                         categories=subject_info['categories'])

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('vip_folder', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)