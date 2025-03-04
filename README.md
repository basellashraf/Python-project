# System Tool

## Description
This Python tool provides a simple command-line interface to perform essential system tasks. It offers options to monitor system resources, list directory contents, and exit the tool.

## Features
- **Monitor System Resources:** Displays device hostname, IP address, and disk usage statistics (total, used, and free space).
- **List Directory Contents:** Lists all files and directories in a given path, distinguishing between files and folders.
- **Exit the Tool:** Safely exit the application.

## Usage
1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python system_tool.py
```

3. Follow the on-screen instructions to choose a task:

- Press **1** to monitor system resources.
- Press **2** to list directory contents.
- Press **3** to exit the tool.

## Example Output

```
Hi!, Welcome to our tool

These are our menu of tasks:

Task [1]: Monitor System Resources.
Task [2]: List Directory Contents.
Task [3]: Exit the Tool.
```

## Requirements
- Python 3.x

Built-in libraries used:
- `os`
- `shutil`
- `socket`

## Notes
- Make sure you run the tool with the necessary permissions to access directories or system info.
- If an invalid input is provided, the tool will prompt you again until a valid option is chosen.

## License
This project is licensed under the MIT License.

