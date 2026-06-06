# This file creates the GUI window

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
from scanner import scan_file, scan_folder
from quarantine import quarantine_file, list_quarantine
from monitor import start_monitor

# Colors
BG_COLOR = "#1a1a2e"
BUTTON_COLOR = "#16213e"
GREEN = "#00ff88"
RED = "#ff4444"
WHITE = "#ffffff"
YELLOW = "#ffd700"

def create_gui():
    window = tk.Tk()
    window.title("Antivirus Scanner")
    window.geometry("700x500")
    window.configure(bg=BG_COLOR)
    window.resizable(False, False)

    # Title
    title = tk.Label(window,
        text="ANTIVIRUS SCANNER",
        font=("Courier", 24, "bold"),
        bg=BG_COLOR,
        fg=GREEN)
    title.pack(pady=20)

    # Output box
    output = scrolledtext.ScrolledText(window,
        width=70,
        height=15,
        bg="#0d0d1a",
        fg=WHITE,
        font=("Courier", 10))
    output.pack(pady=10)

    def log(message, color=WHITE):
        output.configure(state="normal")
        output.insert(tk.END, message + "\n")
        output.configure(state="disabled")
        output.see(tk.END)

    # Buttons frame
    btn_frame = tk.Frame(window, bg=BG_COLOR)
    btn_frame.pack(pady=10)

    def scan_single():
        filepath = filedialog.askopenfilename()
        if filepath:
            log("\nScanning: " + filepath, WHITE)
            result = scan_file(filepath)
            if result == "INFECTED":
                log("*** VIRUS FOUND ***", RED)
                answer = messagebox.askyesno("Virus Found!", 
                    "Virus detected! Move to quarantine?")
                if answer:
                    quarantine_file(filepath)
                    log("File quarantined!", YELLOW)
            else:
                log("File is CLEAN!", GREEN)

    def scan_folder_gui():
        folderpath = filedialog.askdirectory()
        if folderpath:
            log("\nScanning folder: " + folderpath, WHITE)
            infected = scan_folder(folderpath)
            if infected and len(infected) > 0:
                log("VIRUSES FOUND: " + str(len(infected)), RED)
                answer = messagebox.askyesno("Viruses Found!",
                    "Quarantine all infected files?")
                if answer:
                    for f in infected:
                        quarantine_file(f)
                    log("All infected files quarantined!", YELLOW)
            else:
                log("All files are CLEAN!", GREEN)

    def view_quarantine():
        files = __import__('os').listdir("quarantine")
        log("\nFiles in Quarantine:", YELLOW)
        if len(files) == 0:
            log("Quarantine is empty.")
        else:
            for f in files:
                log("  - " + f)

    def start_monitor_gui():
        folderpath = filedialog.askdirectory()
        if folderpath:
            log("\nMonitoring: " + folderpath, GREEN)
            log("Press Ctrl+C in terminal to stop.", YELLOW)
            t = threading.Thread(target=start_monitor, 
                args=(folderpath,), daemon=True)
            t.start()

    # Buttons
    btn_style = {
        "font": ("Courier", 11, "bold"),
        "bg": BUTTON_COLOR,
        "fg": GREEN,
        "width": 20,
        "height": 2,
        "bd": 0,
        "cursor": "hand2"
    }

    tk.Button(btn_frame, text="Scan File",
        command=scan_single, **btn_style).grid(
        row=0, column=0, padx=5, pady=5)

    tk.Button(btn_frame, text="Scan Folder",
        command=scan_folder_gui, **btn_style).grid(
        row=0, column=1, padx=5, pady=5)

    tk.Button(btn_frame, text="View Quarantine",
        command=view_quarantine, **btn_style).grid(
        row=0, column=2, padx=5, pady=5)

    tk.Button(btn_frame, text="Real Time Monitor",
        command=start_monitor_gui, **btn_style).grid(
        row=1, column=1, padx=5, pady=5)

    window.mainloop()

create_gui()