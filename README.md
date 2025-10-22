# argon2-login-demo

> This program demonstrates the capabilities of Argon2 Password Hashing in Python.

## Features

- User registration with password confirmation
- Secure login with Argon2 password hashing
- SQLite database storage
- Clean CLI interface
- Input validation and error handling

## Prerequisites

- Python 3.11 or later
- pip (Python package installer)

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/RIODABERD/argon2-login-demo.git
cd argon2-login-demo
```

2. Install required packages:
```bash
pip install argon2-cffi
```

3. Run the program:
```bash
python main.py
```

**Important**: Always run the program through `main.py`, not the individual modules.

## Project Structure

```
login-cli-argon2/
├── main.py           # Entry point - run this file
├── src/
│   ├── __init__.py
│   ├── auth.py      # Authentication logic
│   └── db.py        # Database operations
├── requirements.txt
└── database.db      # Created on first run
```

## Security Features

- Passwords are hashed using Argon2
- No plaintext passwords stored
- SQLite with prepared statements prevents SQL injection
- Input validation
- Password confirmation during registration

## Development Notes

- Database is created automatically on first run
- `database.db` should be in `.gitignore` (not committed)
- Always run through `main.py`