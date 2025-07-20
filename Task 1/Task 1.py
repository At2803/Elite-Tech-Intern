import hashlib
import os
import json
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

HASH_DB_FILE = 'hash_database.json'

def calculate_hash(filepath, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def load_hash_database():
    if os.path.exists(HASH_DB_FILE):
        with open(HASH_DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_hash_database(db):
    with open(HASH_DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

def monitor_directory(directory, log_output):
    hash_db = load_hash_database()
    updated_db = {}

    log_output.insert(tk.END, f"\n[INFO] Scanning directory: {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            file_hash = calculate_hash(filepath)

            updated_db[filepath] = file_hash

            if filepath not in hash_db:
                log_output.insert(tk.END, f"[NEW FILE] {filepath}\n")
            elif hash_db[filepath] != file_hash:
                log_output.insert(tk.END, f"[MODIFIED] {filepath}\n")
            else:
                log_output.insert(tk.END, f"[UNCHANGED] {filepath}\n")

    removed_files = set(hash_db.keys()) - set(updated_db.keys())
    for filepath in removed_files:
        log_output.insert(tk.END, f"[REMOVED] {filepath}\n")

    save_hash_database(updated_db)
    log_output.insert(tk.END, "\n[INFO] Scan complete.\n")
    log_output.see(tk.END)

# GUI Application
def start_gui():
    def browse_directory():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            dir_entry.delete(0, tk.END)
            dir_entry.insert(0, folder_selected)

    def start_scan():
        directory = dir_entry.get().strip()
        if not os.path.isdir(directory):
            messagebox.showerror("Invalid Directory", "Please select a valid directory.")
            return
        log_output.delete('1.0', tk.END)
        monitor_directory(directory, log_output)

    root = tk.Tk()
    root.title("File Integrity Monitor")
    root.geometry("700x500")
    root.resizable(False, False)

    tk.Label(root, text="Select Directory to Monitor:", font=("Arial", 12)).pack(pady=10)

    dir_frame = tk.Frame(root)
    dir_frame.pack(pady=5)

    dir_entry = tk.Entry(dir_frame, width=60, font=("Arial", 10))
    dir_entry.pack(side=tk.LEFT, padx=5)

    browse_btn = tk.Button(dir_frame, text="Browse", command=browse_directory)
    browse_btn.pack(side=tk.LEFT, padx=5)

    scan_btn = tk.Button(root, text="Start Scan", font=("Arial", 12), command=start_scan, bg="#4CAF50", fg="white")
    scan_btn.pack(pady=10)

    log_output = scrolledtext.ScrolledText(root, width=85, height=20, font=("Courier New", 10))
    log_output.pack(pady=10)

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    start_gui()
