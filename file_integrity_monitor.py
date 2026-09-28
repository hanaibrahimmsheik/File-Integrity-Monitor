import hashlib
import os


BASELINE_FILE = "baseline.txt"


def calculate_hash(filename):
    with open(filename, "rb") as file:
        file_data = file.read()

    return hashlib.sha256(file_data).hexdigest()


def create_baseline(filename):
    if not os.path.exists(filename):
        print("\nError: File not found.")
        return

    file_hash = calculate_hash(filename)

    with open(BASELINE_FILE, "w") as file:
        file.write(filename + "\n")
        file.write(file_hash)

    print("\nBaseline created successfully.")
    print("File:", filename)
    print("SHA-256 hash saved.")


def check_integrity(filename):
    if not os.path.exists(filename):
        print("\nWARNING: File not found.")
        print("The file may have been deleted or moved.")
        return

    if not os.path.exists(BASELINE_FILE):
        print("\nError: No baseline found.")
        print("Create a baseline first.")
        return

    with open(BASELINE_FILE, "r") as file:
        saved_filename = file.readline().strip()
        saved_hash = file.readline().strip()

    if filename != saved_filename:
        print("\nError: This file does not match the saved baseline.")
        print("Baseline file:", saved_filename)
        return

    current_hash = calculate_hash(filename)

    if current_hash == saved_hash:
        print("\nFile integrity check: OK")
        print("The file has not been modified.")

    else:
        print("\nWARNING: File has been modified!")
        print("The current hash is different from the original hash.")


while True:
    print("\n================================")
    print("     FILE INTEGRITY MONITOR")
    print("================================")
    print("1. Create baseline")
    print("2. Check file integrity")
    print("3. Exit")
    print("================================")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        filename = input("Enter the file name: ")
        create_baseline(filename)

    elif choice == "2":
        filename = input("Enter the file name: ")
        check_integrity(filename)

    elif choice == "3":
        print("\nExiting program...")
        break

    else:
        print("\nError: Invalid choice. Please select 1, 2, or 3.")