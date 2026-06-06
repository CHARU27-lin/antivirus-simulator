# Main file - This is where everything connects
from monitor import start_monitor
from scanner import scan_file, scan_folder
from quarantine import quarantine_file, restore_file, list_quarantine

def show_menu():
    print("\n" + "=" * 40)
    print("   ANTIVIRUS SCANNER")
    print("=" * 40)
    print("1. Scan a single file")
    print("2. Scan a folder")
    print("3. View quarantine")
    print("4. Restore file from quarantine")
    print("5. Real time monitor")
    print("6. Exit")
    print("=" * 40)

def main():
    print("Antivirus Scanner Starting...")
    
    while True:
        show_menu()
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            filepath = input("Enter full file path: ")
            result = scan_file(filepath)
            if result == "INFECTED":
                answer = input("Move to quarantine? (yes/no): ")
                if answer == "yes" or answer == "y":
                    quarantine_file(filepath)
        
        elif choice == "2":
            folderpath = input("Enter folder path: ")
            infected_files = scan_folder(folderpath)
            if infected_files and len(infected_files) > 0:
                answer = input("Quarantine all infected files? (yes/no): ")
                if answer == "yes" or answer == "y":
                    for f in infected_files:
                        quarantine_file(f)
        
        elif choice == "3":
            list_quarantine()
        
        elif choice == "4":
            filename = input("Enter filename to restore: ")
            original = input("Enter original path to restore to: ")
            restore_file(filename, original)
        
        elif choice == "5":
            folderpath = input("Enter folder path to monitor: ")
            start_monitor(folderpath)
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Enter 1-6")

main()