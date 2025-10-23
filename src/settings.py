# This module defines and parses command-line arguments for configuring Argon2 password hashing parameters.
import getpass
import sys
import argparse

# Preset values in case users do not provide any
DEFAULT_TIME_COST = 3 
DEFAULT_PARALLELISM = 4
DEFAULT_MEMORY_COST = 65536

def parse_arguments(): # Creates an argument parser for options
    parser = argparse.ArgumentParser(
        description="Argon2 Password Hashing Configuration",
        formatter_class=argparse.RawTextHelpFormatter                             
    )

    parser.add_argument( # Time Cost argument. Default Value is 3
        '--time-cost',
        type=int,
        default=DEFAULT_TIME_COST,
        help=f"Sets the Argon2 time cost (T). Must be a positive integer between 1 and 10.\nDefault value: {DEFAULT_TIME_COST}"
    )

    parser.add_argument( # Parallelism argument. Default Value is 4
        '--parallelism',
        type=int,
        default=DEFAULT_PARALLELISM,
        help=f"Sets the Argon2 parallelism (P). Must be a positive integer between 1 and 16.\nDefault value: {DEFAULT_PARALLELISM}"
    )

    parser.add_argument( # Memory Cost argument. Default Value is 65536 KiB (64 MiB)
        '--memory-cost',
        type=int,
        default=DEFAULT_MEMORY_COST,
        help=f"Sets the Argon2 memory cost (M) in kibibytes. Must be a positive integer.\nDefault value: {DEFAULT_MEMORY_COST}"
    )

    parser.add_argument( # Show Password argument. Default is False
        '--show-password',
        action='store_true',
        default=False,
        help="If set, passwords will be shown in plaintext when typed (for debugging purposes)."
    )

    parser.add_argument( # Show Hash argument. Default is False
        '--show-hash',
        action='store_true',
        default=False,
        help="If set, the hashed password will be displayed upon registration (for debugging purposes)."
    )

    args = parser.parse_args()

    if not (1 <= args.time_cost <= 10): # Error handling for invalid inputs in time cost
        parser.error("[Error] Time cost must be between 1 and 10.")
        sys.exit(2)

    if not (1 <= args.parallelism <= 16): # Error handling for invalid inputs in parallelism
        parser.error("[Error] Parallelism must be between 1 and 16.")
        sys.exit(3)

    if not (args.memory_cost > 0): # Error handling for invalid inputs in memory cost
        parser.error("[Error] Memory cost must be a positive integer.")
        sys.exit(4)

    return args

def get_input(prompt, is_secret): # Get user input, optionally hiding it for passwords
    if not is_secret:
        return getpass.getpass(prompt)
    else:
        return input(prompt)

def show_hash(username, hashed_password):
    if not (parse_arguments().show_hash):
        return
    else:
        return print(f"\n[✔]User {username} registered with hashed password: {hashed_password}")
