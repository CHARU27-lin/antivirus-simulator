# This file moves infected files to quarantine folder

import os
import shutil

QUARANTINE_FOLDER = "quarantine"

def quarantine_file(filepath):
    try:
        filename = os.path.basename(filepath)
        
        destination = os.path.join(QUARANTINE_FOLDER, filename)
        
        shutil.move(filepath, destination)
        
        print("File moved to quarantine: " + filename)
        return True
    
    except FileNotFoundError:
        print("Error: File not found!")
        return False
    
    except Exception as e:
        print("Error: " + str(e))
        return False

def restore_file(filename, original_path):
    try:
        source = os.path.join(QUARANTINE_FOLDER, filename)
        
        shutil.move(source, original_path)
        
        print("File restored to: " + original_path)
        return True
    
    except FileNotFoundError:
        print("Error: File not found in quarantine!")
        return False

def list_quarantine():
    print("\nFiles in Quarantine:")
    print("=" * 40)
    
    files = os.listdir(QUARANTINE_FOLDER)
    
    if len(files) == 0:
        print("Quarantine is empty.")
    else:
        for f in files:
            print("- " + f)
    
    print("=" * 40)