# This file saves scan results to a report

import os
from datetime import datetime

REPORT_FOLDER = "reports"

def create_report(clean_files, infected_files):
    
    os.makedirs(REPORT_FOLDER, exist_ok=True)
    
    now = datetime.now()
    filename = "scan_" + now.strftime("%Y%m%d_%H%M%S") + ".txt"
    filepath = os.path.join(REPORT_FOLDER, filename)
    
    with open(filepath, "w") as f:
        f.write("=" * 40 + "\n")
        f.write("ANTIVIRUS SCAN REPORT\n")
        f.write("=" * 40 + "\n")
        f.write("Date: " + now.strftime("%Y-%m-%d") + "\n")
        f.write("Time: " + now.strftime("%H:%M:%S") + "\n")
        f.write("=" * 40 + "\n\n")
        
        f.write("CLEAN FILES: " + str(len(clean_files)) + "\n")
        for cf in clean_files:
            f.write("  [CLEAN] " + cf + "\n")
        
        f.write("\nINFECTED FILES: " + str(len(infected_files)) + "\n")
        for inf in infected_files:
            f.write("  [VIRUS] " + inf + "\n")
        
        f.write("\n" + "=" * 40 + "\n")
        f.write("Total scanned: " + str(len(clean_files) + len(infected_files)) + "\n")
        f.write("=" * 40 + "\n")
    
    print("\nReport saved: " + filepath)
    return filepath