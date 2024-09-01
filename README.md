# APK Analyzer

This project provides a simple Python script to analyze Android APK files using the `androguard` library. The script extracts various metadata from the APK, including package name, version, permissions, and more.

## Prerequisites

- Python 3.x
- `androguard` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tinmaungzin/inspect-apk.git
    cd inspect-apk
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Configure the APK Path:**

    Replace the APK path in the script with the path to the APK file you want to analyze.

    ```python
    apk_analyzer = APKAnalyzer("/path/to/your.apk")
    ```

2. **Run the Script:**

    Execute the script to analyze the APK and print the metadata:

    ```bash
    python app.py
    ```


## Script Behavior

- **Package Name:** Retrieves the package name of the APK.
- **Version Name:** Gets the version name of the APK.
- **Version Code:** Obtains the version code of the APK.
- **Permissions:** Lists the permissions requested by the APK.
- **Main Activity:** Finds the main activity of the APK.
- **Signature:** Retrieves the APK's signature.

## Code Overview

- **Initialization:** Loads the APK file using `androguard`.
- **Metadata Extraction:** Provides methods to extract various pieces of information from the APK.
- **Analysis:** Gathers all extracted information into a dictionary and returns it.

## Example Output

When running the script, you will get an output similar to the following:

```json
{
    'package_name': 'com.example.app',
    'version_name': '1.0.0',
    'version_code': 1,
    'permissions': [
        'android.permission.INTERNET',
        'android.permission.ACCESS_NETWORK_STATE'
    ],
    'main_activity': 'com.example.app.MainActivity',
    'signature': '1234567890abcdef'
}
```

## Troubleshooting

- **APK File Issues:** Ensure the APK file path is correct and the file is accessible.
- **Library Issues:** Verify that the androguard library is properly installed and compatible with your Python version.
