# This file watches a folder for new files automatically

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from scanner import scan_file
from quarantine import quarantine_file

class AntivirusHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        print("\n*** NEW FILE DETECTED: " + filepath + " ***")
        
        time.sleep(1)
        
        result = scan_file(filepath)
        
        if result == "INFECTED":
            print("*** DANGEROUS FILE! Moving to quarantine... ***")
            quarantine_file(filepath)
        else:
            print("File is safe!")

def start_monitor(folderpath):
    print("\n" + "=" * 40)
    print("REAL TIME MONITOR STARTED")
    print("Watching: " + folderpath)
    print("Press Ctrl+C to stop")
    print("=" * 40)
    
    event_handler = AntivirusHandler()
    observer = Observer()
    observer.schedule(event_handler, folderpath, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitor stopped!")
    
    observer.join()