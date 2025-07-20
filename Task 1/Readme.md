File Integrity Monitor

A simple yet powerful Python-based File Integrity Monitoring (FIM) tool with a user-friendly Tkinter GUI. This application helps detect any new, modified, or deleted files within a selected directory by calculating and comparing cryptographic file hashes.

## Features

- Monitor any folder recursively
- Uses SHA-256 hash algorithm to detect changes
- Detects:
  - New files
  - Modified files
  - Removed files
  - Unchanged files
- Automatically saves hash database in a JSON file
- User-friendly GUI using Tkinter
- Scrollable log display with real-time scan output

---

## How It Works

1. Select a directory using the "Browse" button.
2. Click "Start Scan".
3. The tool will compare current file hashes with previously saved hashes in hash_database.json.
4. Displays the result for each file (NEW, MODIFIED, REMOVED, UNCHANGED).
5. Saves updated hashes for the next scan.

---

## Requirements

- Python 3.6+
- Tkinter (usually comes pre-installed with Python)

---

##
Run the Application
python file_integrity_monitor.py

---

##
File Structure
file-integrity-monitor/
│
├── file_integrity_monitor.py   # Main application script
├── hash_database.json          # Auto-generated hash database
└── README.md                   # This file
