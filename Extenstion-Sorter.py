import os
import shutil

def move_files(source_dir, dest_dir, file_extension):
    # Ensure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Walk through all directories and subdirectories
    for root, _, files in os.walk(source_dir):
        for filename in files:
            # Check if the file ends with the specified extension
            if filename.endswith(file_extension):
                # Construct full file path
                source_file = os.path.join(root, filename)
                dest_file = os.path.join(dest_dir, filename)
                
                # Handle duplicates
                duplicate_count = 1
                while os.path.exists(dest_file):
                    duplicate_dir = os.path.join(dest_dir, f'duplicates_{duplicate_count}')
                    if not os.path.exists(duplicate_dir):
                        os.makedirs(duplicate_dir)
                    dest_file = os.path.join(duplicate_dir, filename)
                    duplicate_count += 1
                
                # Move the file
                shutil.move(source_file, dest_file)
                print(f'Moved: {source_file} to {dest_file}')

# Example usage
source_directory = os.getcwd()
destination_directory = os.path.join(os.getcwd(), 'Herolab-Files')
file_ext = '.por'  # Change this to the desired file extension

move_files(source_directory, destination_directory, file_ext)