"""
Organises a chosen directory by grouping files into folders.
"""

import os
import shutil

FOLDER_TO_EXTENSIONS = {
    'Applications': ['.app', '.dmg'],
    'Documents': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.heic'],
    'Media': ['.mp3', '.mp4', '.mov', '.gif'],
    'Archives': ['.zip'],
    'TextFiles': ['.txt', '.html', '.htm', '.css', '.js'],
    'Configurations': ['.plist']
}


def main():
    directory = get_valid_directory()
    display_files(directory)
    files = get_files(directory)
    sort_files(files, directory)
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
    files = get_files(directory)
    print(f"\n-----Files-----\n")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file.strip()}")
    print(f"Total of {len(files)} file(s)")
    print(f"\n-----Files-----\n")


def get_files(directory):
    """Get files from directory."""
    files = os.listdir(directory)
    return files


def create_folder(folder_name):
    """Create a folder."""
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")


def sort_files(files, directory):
    """Sort files by allocation to folder."""
    # Create folders
    for folder in FOLDER_TO_EXTENSIONS.keys():
        create_folder(os.path.join(directory, folder))

    for file in files:
        #  '_' throwaway variable for prefix
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        # Check if the extension is in any of the specified folders
        is_moved = False
        for folder, extensions in FOLDER_TO_EXTENSIONS.items():
            if extension in extensions:
                folder_path = os.path.join(directory, folder, file)
                # Check if the file already exists in the target folder
                if not os.path.exists(folder_path):
                    shutil.move(os.path.join(directory, file), folder_path)
                    is_moved = True

        # If the file doesn't match any specified extensions, move it to the 'Other' folder
        if not is_moved:
            create_folder(os.path.join(directory, 'Other'))
            folder_path = os.path.join(directory, 'Other', file)
            shutil.move(os.path.join(directory, file), folder_path)


main()
