# This file scans files and folders
from report import create_report
import os
from hasher import hash_file
from signatures import check_signature

def scan_file(filepath):
    print("\nScanning: " + filepath)
    
    file_hash = hash_file(filepath)
    
    if file_hash is None:
        print("Could not scan this file.")
        return
    
    print("Hash: " + file_hash)
    
    is_malware, virus_name = check_signature(file_hash)
    
    if is_malware:
        print("*** VIRUS FOUND: " + virus_name + " ***")
        return "INFECTED"
    else:
        print("File is CLEAN")
        return "CLEAN"

def scan_folder(folderpath):
    print("\nScanning folder: " + folderpath)
    print("=" * 40)

    infected = []
    clean = []
    
    for filename in os.listdir(folderpath):
        filepath = os.path.join(folderpath, filename)
        
        if os.path.isfile(filepath):
            result = scan_file(filepath)
            if result == "INFECTED":
                infected.append(filepath)
            elif result == "CLEAN":
                clean.append(filepath)
    
    print("\n" + "=" * 40)
    print("SCAN COMPLETE")
    print("Clean files: " + str(len(clean)))
    print("Infected files: " + str(len(infected)))
    
    create_report(clean, infected)
    return infected