import os

# Define the directory containing the files
directory = r"C:\PNG\MMDD"

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file name is longer than 2 characters
    if len(filename) > 2:
        # Construct the new file name by removing the first two characters
        new_filename = filename[2:]
        
        # Construct the full file paths
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} to {new_filename}")

print("File renaming completed.")
