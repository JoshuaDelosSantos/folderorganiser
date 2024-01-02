"""
Organises a chosen directory by grouping files into folders.
"""

import os


def main():
    directory = get_valid_directory()
    display_files(directory)
    print("Command executed")


def get_valid_directory():
    """Get a valid directory."""
    directory = input("Directory to organise: ")
    is_valid_directory = os.path.exists(directory)
    print(f"Is valid: {is_valid_directory}")
    while not is_valid_directory:
        directory = input("Directory to organise: ")
        is_valid_directory = os.path.exists(directory)
        print("Invalid Directory!")

    return directory


def display_files(directory):
    """Display file in a formatted way from a directory."""
    files = os.listdir(directory)
    for file in files:
        print(file.strip())


# def sort_files():
#     for file in files:
#         os.

main()
