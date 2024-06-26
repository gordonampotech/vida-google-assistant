from flask import Flask, render_template, request
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save_configuration', methods=['POST'])
def save_configuration():
    project_id = request.form['project_id']
    json_file = request.files['json_file']

    if not project_id or not json_file:
        return "Project ID and JSON file are required", 404

    try:
        # Define paths
        config_file_path = '/homeassistant/configuration.yaml'
        json_file_save_path = '/homeassistant/SERVICE_ACCOUNT.JSON'

        # Check if configuration.yaml exists
        if not os.path.exists(config_file_path):
            return f"{config_file_path} does not exist", 500

        # Read the current configuration.yaml
        with open(config_file_path, 'r') as config_file:
            config_content = config_file.read()

        # Define the new configuration to be added
        new_config = f"""
google_assistant:
  project_id: {project_id}
  service_account: !include SERVICE_ACCOUNT.JSON
  report_state: true
"""

        # Check if the google_assistant configuration already exists
        pattern = re.compile(r'google_assistant:\n(?: {2}.*\n)*', re.MULTILINE)

        if pattern.search(config_content):
            # If it exists, replace the existing google_assistant section
            config_content = pattern.sub(new_config, config_content)
        else:
            # If it does not exist, append the new configuration
            config_content += '\n' + new_config

        # Write the updated configuration back to configuration.yaml
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)

        # Save the JSON file
        json_file.save(json_file_save_path)

        return f"Configuration added or updated and file saved", 200

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
