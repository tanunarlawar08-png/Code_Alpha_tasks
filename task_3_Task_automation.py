import os
import shutil

# Define source and destination folders
source_folder = "camera roll"
destination_folder = "images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created folder: {destination_folder}")

# Check if source folder exists
if not os.path.exists(source_folder):
    print(f"Error: {source_folder} folder not found!")
else:
    # Get all files in source folder
    files = os.listdir(source_folder)
    
    # Counter for moved files
    moved_count = 0
    
    # Loop through each file
    for file in files:
        # Check if file is a .jpg file
        if file.endswith('.jpg') or file.endswith('.jpeg'):
            # Get full path of source file
            source_path = os.path.join(source_folder, file)
            # Get full path of destination file
            destination_path = os.path.join(destination_folder, file)
            
            # Move the file
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")
            moved_count += 1
    
    # Print summary
    print(f"\nTotal files moved: {moved_count}")
