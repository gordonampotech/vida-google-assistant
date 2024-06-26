from flask import Flask, render_template, request
from flask_cors import CORS
import os

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
        return "Project ID and JSON file are required", 400

    try:
        # Define paths
        config_file_path = '/usr/share/hassio/homeassistant/configuration.yaml'
        json_file_save_path = f'/usr/share/hassio/homeassistant/{json_file.filename}'

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

        # Check if the configuration already exists in the file
        if new_config.strip() in config_content:
            return "Configuration already exists in configuration.yaml", 200

        # Append new configuration to configuration.yaml
        with open(config_file_path, 'a') as config_file:
            config_file.write(new_config)

        # Save the JSON file
        json_file.save(json_file_save_path)

        return f"Configuration added and file saved as {json_file_save_path}"

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
