# This file calculates the hash of any file

import hashlib

def hash_file(filepath):
    md5 = hashlib.md5()
    
    try:
        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                md5.update(chunk)
        
        return md5.hexdigest()
    
    except FileNotFoundError:
        print("Error: File not found!")
        return None
    
    except PermissionError:
        print("Error: Cannot access this file!")
        return None