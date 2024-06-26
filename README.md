# Vida Google Assistant Add-on

This Add-On helps users set up their `project_id` and upload the service account JSON file for integration with Google Assistant.

![Vida Google Assistant Add-on](images/screenshot.png)

## About

The Vida Google Assistant Add-on is a tool for your Home Assistant device that simplifies the process of integrating Google Assistant by allowing you to easily add your `project_id` and service account JSON file. Once the JSON file is uploaded and the project ID is provided, the add-on automatically updates the `configuration.yaml` file to include the necessary Google Assistant configuration.

### Key Features

- **Simple Setup**: Quickly add your Google Assistant `project_id` and upload the service account JSON file.
- **Automated Configuration**: Automatically updates `configuration.yaml` with the necessary configuration for Google Assistant.
- **Secure and Efficient**: Ensures that your Home Assistant setup remains updated and secure with minimal effort.

## Installation and Usage

1. **Download and Install the Add-On**: Install the add-on via the Home Assistant Add-on store or manually from the provided repository.
2. **Open the Web UI**: Navigate to the add-on's web UI from the Home Assistant interface.
3. **Enter Project ID and Upload JSON File**:
    - Enter your Google Assistant `project_id`.
    - Upload the service account JSON file.
4. **Submit and Apply**:
    - Click the submit button to update `configuration.yaml` and upload the JSON file.
5. **Restart Home Assistant**: Restart your Home Assistant instance to apply the new configuration.

### Example Configuration

After submission, your `configuration.yaml` will include:

```yaml
google_assistant:
  project_id: YOUR_PROJECT_ID
  service_account: !include YOUR_JSON_FILE.json
  report_state: true
```