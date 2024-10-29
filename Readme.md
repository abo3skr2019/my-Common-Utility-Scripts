# File Management Utilities

This repository contains a collection of Python scripts for managing and organizing files that i use in conjunction czkawka.
Each script performs a specific task such as deleting duplicates, sorting files by extension, organizing files by prefix, and more.

## Scripts

### 1. duplicate-deleter

This script finds and handles duplicate files in a given directory.

- **Functions:**
  - `calculate_file_hash(file_path)`: Calculates the SHA-256 hash of a file.
  - `find_duplicates(cwd)`: Finds duplicate files in the given directory and subdirectories.
  - `move_duplicates_to_delete(duplicates)`: Moves duplicates to the 'to-be-deleted' directory.
  - `main()`: Main function to execute the script.

### 2. emptyfolder-Deleter

This script deletes empty folders in a given directory.

### 3. Extenstion-Sorter

This script sorts files based on their extensions and moves them to specified directories.

- **Functions:**
  - `move_files(source_dir, dest_dir, file_extension)`: Moves files with a specific extension from the source directory to the destination directory.

### 4. Folder-Sorter

This script groups files based on name similarity and moves them to grouped directories.

### 5. hrefParser

This script extracts and saves href links from HTML files.

- **Functions:**
  - `extract_hrefs(file_path)`: Extracts href links from an HTML file.
  - `save_hrefs_to_file(hrefs, output_file)`: Saves extracted href links to a file.

### 6. Prefix-Matcher

This script organizes files by their prefixes and moves them to respective directories.

- **Functions:**
  - `organize_files_by_prefix(exclude_dirs=None)`: Organizes files by their prefixes, excluding specified directories.

### 7.PDFConverter

This Script Converts Office 365 Formats into PDFs

## Usage

Each script can be executed independently. For example, to run the `duplicate-deleter` script, use the following command:

```sh
python duplicate-deleter 
```
