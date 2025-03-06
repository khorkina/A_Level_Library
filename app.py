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
        'folder': 'Business_Materials'
    },
    'psychology': {
        'name': 'Psychology A-Level',
        'description': 'In-depth psychology resources',
        'folder': 'Psyhology_Materials'  # Keeping original spelling from zip file
    },
    'sociology': {
        'name': 'Sociology A-Level',
        'description': 'Essential sociology study materials',
        'folder': 'Sociology_Materials'
    },
    'english': {
        'name': 'English A-Level',
        'description': 'Literature and language resources',
        'folder': 'English_Materials'
    }
}

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
                pdfs.append({
                    'name': name,
                    'filename': rel_path
                })
    return sorted(pdfs, key=lambda x: x['name'])

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
                         pdfs=pdfs)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('vip_folder', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)