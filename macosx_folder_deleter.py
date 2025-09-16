import os
import shutil

def delete_macosx_folders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__MACOSX' in dirnames:
            macosx_path = os.path.join(dirpath, '__MACOSX')
            shutil.rmtree(macosx_path)
            print(f"Deleted: {macosx_path}")

if __name__ == "__main__":
    root_directory = os.getcwd()
    delete_macosx_folders(root_directory)