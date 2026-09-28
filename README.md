# File Integrity Monitoring System

A beginner-friendly Python cybersecurity project that monitors files for unauthorized changes using SHA-256 hashing.

## Features

- Create a baseline SHA-256 hash for a file
- Check whether a file has been modified
- Detect missing or deleted files
- Compare the current file hash with the saved baseline
- Verify that the checked file matches the saved baseline
- Simple command-line interface
- Basic input validation and error handling

## Technologies Used

- Python
- hashlib
- SHA-256
- VS Code
- GitHub

## How It Works

The program creates a SHA-256 hash of the selected file and stores it as a baseline.

When the file is checked later, the program calculates its SHA-256 hash again and compares it with the saved baseline.

### If the hashes match

The file has not been modified.

### If the hashes are different

The program reports that the file has been modified.

### If the file is missing

The program reports that the file may have been deleted or moved.

## How to Run

Run the program using:

```bash
uv run python file_integrity_monitor.py