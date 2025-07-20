# Penetration Testing Toolkit (GUI-Based)

A simple, beginner-friendly penetration testing toolkit built with Python and Tkinter, featuring two core modules:
- *Port Scanner*
- *Brute Force (SSH Simulator)*

This toolkit is designed for educational and demonstration purposes only and provides a clean GUI to explore basic network security concepts.

---

## Features

- GUI-based interaction with dropdown menu
- Fast multithreaded *Port Scanner* (1–1024)
- Simulated *Brute Force Attack* using a custom wordlist
- Real-time scan output using ScrolledText
- Dark-themed, modern-looking interface using Tkinter

---

## File Structure

pentest-toolkit/

│
├── main.py # Main launcher GUI

├── port_scanner.py # Port scanning module

├── brute_forcer.py # Brute force simulator module

├── assets/

│ └── wordlist.txt # Wordlist for brute force attacks

└── README.md # Project documentation

---

## How to Run

### Prerequisites

- Python 3.6+
- No external libraries required (Tkinter, socket, concurrent.futures are all standard)

### Running the Toolkit

# Clone the repository
cd pentest-toolkit

# Run the application
python main.py

---

## Sample Wordlist (assets/wordlist.txt)
admin

123456

letmein

qwerty

password

admin123

testpass
