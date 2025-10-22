# This module handles user authentication and registration using Argon2 for password hashing.

from argon2 import PasswordHasher
import sqlite3

ph = PasswordHasher()

class UsernameDuplicateError(Exception):
    pass

def authenticate(db: str, username: str, password: str) -> bool:
    # Verify username/password against the stored Argon2 hash.
    from src.db import db_cursor
    with db_cursor(db, commit=False) as cursor:
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone() 
        if row is None:
            return False
        stored_hash = row[0]

    try:
        # verify() expects the stored hash and the user-input password
        return ph.verify(stored_hash, password)
    except Exception:
        return False
    
def register(db: str, username: str, password: str) -> int:

    hashed_password = ph.hash(password) # hash the password using Argon2

    # for debugging purposes you can uncomment the next line, but avoid printing hashes in production
    # print(f"User {username} registered with hashed password: {hashed_password}")

    # store the hashed password and username in the database
    try:
        from src.db import db_cursor
        with db_cursor(db, commit=True) as cursor:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            return cursor.lastrowid
    except sqlite3.IntegrityError: # Catch duplicate username
        raise UsernameDuplicateError(f"Username {username} already exists.")
    

if __name__ == "__main__":
    # Prevent running this module directly; `main.py` is the intended entrypoint.
    import sys
    print("Do not run this file directly. Run the application via 'python main.py' from the project root.")
    sys.exit(1)
