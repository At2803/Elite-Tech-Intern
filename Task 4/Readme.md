# File Encryption Tool (GUI)

A robust, user-friendly Python application that allows you to *securely encrypt and decrypt files* using *AES-256 (CBC mode)* with a password. Built with Tkinter for a clean GUI and powered by PyCryptodome for modern cryptographic security.

---

## Features

- AES-256 encryption (CBC mode) using PBKDF2 key derivation
- Password-protected file encryption/decryption
- File selector with encryption and decryption buttons
- Clean, simple, and intuitive Tkinter GUI
- Reset feature to clear selections
- Salt + IV included for enhanced security

---

## Requirements

- Python 3.6+

### Install dependencies:

pip install pycryptodome

---

##Run the application:-

python encryption_tool.py

---

## File Overview:-

encryption-tool/

│
├── encryption_tool.py       # Main GUI application script

└── README.md                # This file

---

## How It Works
Key Derivation:
Uses PBKDF2 with a random 16-byte salt and 1 million iterations to derive a 256-bit key from the password.

a)Encryption Process:-

1.Pads data to AES block size

2.Uses random IV for each file

3.Saves output as: salt + iv + ciphertext

b)Decryption Process:-

1.Extracts salt and IV from the encrypted file

2.Derives the key again using password + salt

3.Decrypts and unpads the data
