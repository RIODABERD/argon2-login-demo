# This module initializes the database for the login CLI application.

import sqlite3

def init_db(db: str) -> None:
    with sqlite3.connect(db) as conn:
        # Initialize the users table if it doesn't exist
        cursor = conn.cursor()
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL
                    )
                """)
        conn.commit()

if __name__ == "__main__":
    # Prevent running this module directly; `main.py` is the intended entrypoint.
    import sys
    print("Do not run this file directly. Run the application via 'python main.py' from the project root.")
    sys.exit(1)