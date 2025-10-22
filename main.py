import getpass
import sys
from src.__init__ import init_db
from src.auth import UsernameDuplicateError, authenticate, register

DB = "database.db"

def main():
    while True:
        print("\nLogin System Demo w/ Argon2 Password Hashing\n" 
        "----------------------------------------------" 
        "\n1. Login" 
        "\n2. Register" 
        "\n3. Exit")
        choice = input("Select an option: ")
        match choice:
            case "1": # Login
                login()
            case "2": # Register
                create_user()
            case "3": # Exit
                print("\nExiting program...")
                sys.exit(0)
            case _:
                print("Invalid option. Please try again.")

def login():
    print("\nLogin"
    "\n----------------------------------------------")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    success = authenticate(DB, username, password)
    if success:
        print("\n[✔]Login successful!")
    else:
        print("\n[✖]Login failed. Incorrect username or password.")

def create_user():
    print("\nCreate an Account"
    "\n----------------------------------------------")
    username = input("Choose a username: ")

    while True: # Prompt for password until valid
        password = getpass.getpass("Choose a password: ")
        if not password: # Check for empty password
            print("\n[✖]Password cannot be empty. Please try again.")
            continue

        if password != (confirm_password := getpass.getpass("Confirm password: ")): # Check for match
            print("\n[✖]Passwords do not match. Please try again.")
            continue
        break # Exit loop if password is valid

    try:
        register(DB, username, password)
        print(f"\n[✔]User {username} created successfully.")
    except UsernameDuplicateError: # Catch duplicate username
        print(f"\n[✖]Error: Username {username} already exists.")
    except ValueError as e: # Catch other registration errors
        print(f"\n[✖]Error creating user: {e}")

if __name__ == "__main__":
    init_db(DB)   # create database if it doesn't exist
    main()