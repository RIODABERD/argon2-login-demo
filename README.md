# Argon2 Secure Login Demo

This program demonstrates the capabilities of Argon2 Password Hashing in Python.

---

## Features

- User registration with password confirmation
- Secure login with Argon2 password hashing
- Arguments for customizability
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

## Configuration & Usage

The application is designed as a Command-Line Interface (CLI). All security parameters and developer tools are exposed via command-line arguments

To configure, simply pass the desired argument and value when running `main.py`.
(i.e `python main.py --timecost 5 --parallelism 12 --memory-cost 64000 --show-password --show-hash`)

| flags             | type   | default | description                                                                               |
| ----------------- | ------ | ------- | ----------------------------------------------------------------------------------------- |
| `--time-cost`     | `int`  | `3`     | Sets the Argon2 time cost (T). Must be a positive integer between 1 and 10.               |
| `--parallelism`   | `int`  | `4`     | Sets the Argon2 parallelism (P). Must be a positive integer between 1 and 16              |
| `--memory-cost`   | `int`  | `65536` | Sets the Argon2 memory cost (M) in kibibytes. Must be a positive integer.                 |
| `--show-password` | `flag` | `False` | If set, passwords will be shown in plaintext when typed (for debugging purposes).         |
| `--show-hash`     | `flag` | `False` | If set, the hashed password will be displayed upon registration (for debugging purposes). |



## Project Structure

```
login-cli-argon2/
├── main.py          # Entry point - run this file
├── src/
│   ├── __init__.py  # Initialize database (if non-existent)
│   ├── auth.py      # Authentication logic
│   ├── db.py        # Database operations
│   └── settings.py  # Password hashing configurations
├── requirements.txt
└── database.db      # Created on first run
```

## Security Features

- Passwords are hashed using Argon2
- No plaintext passwords stored
- Password confirmation during registration

## Development Notes

- Database is created automatically on first run
- `database.db` should be in `.gitignore` (not committed)
- Always run through `main.py`

---

## Planned Features

This demo is actively being developed. The following features are planned for the next release, allowing deeper configuration and security testing:

- **Logging:** Integration of the standard Python `logging` module with a configurable verbosity level.
- **Re-hashing:** Create a flag for updating your already hashed passwords.
- **User menu:** An interactive CLI after successfully logging in. Let's users have the ability to change passwords and such.