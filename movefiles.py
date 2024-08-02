import os
import shutil
import csv

def read_csv_extract_identifier(csv_file_path):
    identifier = []
    with open(csv_file_path, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            for path in line:
                identifier.append(os.path.basename(path).split('.')[0])
        return identifier
        

def find_and_move_folder(root_directory, identifiers, destination_directory):
    for subdir, dirs, files in os.walk(root_directory):
        for identifier in identifiers:
            if identifier in subdir:
                source_folder_path = subdir
                destination_folder_path = os.path.join(destination_directory, os.path.basename(subdir))
                # Move the folder
                try:
                    shutil.move(source_folder_path, destination_folder_path)
                    print(f"Moved {source_folder_path} to {destination_folder_path}")
                except Exception as e:
                    print(f"Error moving {source_folder_path}: {e}")

               

# Define file paths
csv_file_path = r"E:\bad_files.csv"
root_directory = r"E:\Final Data\slice_fullimage"
destination_directory = r"E:\Final Data\bad_images\masks"

# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Execute the process
identifier = read_csv_extract_identifier(csv_file_path)
find_and_move_folder(root_directory, identifier, destination_directory)







