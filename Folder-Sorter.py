import os
import shutil
import re
from collections import defaultdict, Counter
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Path to your main directory
root_dir = os.getcwd()
threshold = 70  # Similarity threshold for grouping (0-100)
grouped_dir = os.path.join(root_dir, 'Grouped_Files')

# Create a main directory to hold all grouped subdirectories
os.makedirs(grouped_dir, exist_ok=True)

# Get all files from root_dir and subdirectories, excluding Python files
all_files = []
for dirpath, _, filenames in os.walk(root_dir):
    for file in filenames:
        if not file.endswith('.py'):
            all_files.append(os.path.join(dirpath, file))

# Group files based on name similarity
groups = defaultdict(list)

for file in all_files:
    filename = os.path.basename(file)
    # Find the most similar file name in groups
    matched_group = process.extractOne(filename, groups.keys(), scorer=fuzz.token_set_ratio)
    
    if matched_group and matched_group[1] > threshold:
        groups[matched_group[0]].append(file)
    else:
        groups[filename].append(file)

# Create subdirectories with the most common word as group names
for group_name, files in groups.items():
    # Extract words from all filenames in the group
    words = []
    for file in files:
        filename = os.path.splitext(os.path.basename(file))[0]  # Remove extension
        words.extend(re.findall(r'\w+', filename))  # Extract words
    
    # Find the most common word in the group
    most_common_word = Counter(words).most_common(1)[0][0]
    
    # Create a directory for the group with the most common word as its name
    group_dir = os.path.join(grouped_dir, most_common_word)
    os.makedirs(group_dir, exist_ok=True)
    
    for file in files:
        # Move each file to the new group directory
        try:
            shutil.move(file, os.path.join(group_dir, os.path.basename(file)))
        except shutil.Error as e:
            print(f"Error moving file {file}: {e}")