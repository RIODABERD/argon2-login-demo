from contextlib import contextmanager
from typing import Iterator
import sqlite3 

# Context manager for database connection
@contextmanager
def db_connect(db: str) -> Iterator[sqlite3.Connection]: 
    # Establish connection and yield it, then ensure closure
    conn = sqlite3.connect(db)
    try: 
        yield conn
    finally:
        conn.close()

# Context manager for database cursor
@contextmanager
def db_cursor(db: str, commit: bool = True) -> Iterator[sqlite3.Cursor]: 
    # Provide cursor and handle commit/rollback, then ensure closure
    with db_connect(db) as conn:
        cursor = conn.cursor()
        try: 
            yield cursor
            if commit:
                conn.commit()
        except Exception:
            if commit:
                conn.rollback()
            raise
        finally: 
            try:
                cursor.close()
            except Exception:
                pass

if __name__ == "__main__":
    # Prevent running this module directly; `main.py` is the intended entrypoint.
    import sys
    print("Do not run this file directly. Run the application via 'python main.py' from the project root.")
    sys.exit(1)