import os
import shutil

def organize_files_by_extension(directory_path):

    # 1. Check if the path is a valid directory.
    if not os.path.isdir(directory_path):
        print(f"Error: The path '{directory_path}' is not a valid directory.")
        return

    print(f"Organizing files in: {directory_path}\n")

    # 2. List everything in the directory.
    try:
        all_items = os.listdir(directory_path)
    except OSError as e:
        print(f"Error: Could not access the directory. {e}")
        return

    # 3. Go through each item in the directory.
    for filename in all_items:
        source_path = os.path.join(directory_path, filename)
        if os.path.isdir(source_path):
            continue
        if filename == os.path.basename(__file__):
            print(f"Skipping the script file: {filename}")
            continue

        # Split by the file name and file extension
        _, file_extension = os.path.splitext(filename)

        if not file_extension:
            folder_name = "No_Extension"
        else:
            folder_name = file_extension[1:].lower() + "_files"

        # Destination folder
        destination_folder_path = os.path.join(directory_path, folder_name)
        if not os.path.exists(destination_folder_path):
            try:
                os.makedirs(destination_folder_path)
                print(f"Created folder: {destination_folder_path}")
            except OSError as e:
                print(f"Error creating directory {destination_folder_path}: {e}")
                continue

        # Move the file
        destination_path = os.path.join(destination_folder_path, filename)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}  ->  {folder_name}/")
        except (shutil.Error, OSError) as e:
            print(f"Error moving {filename}: {e}")


print("--- Simple File Organizer ---")
print("This App will organize files in a directory into folders based on their extension.")

organizePath = input("\nPlease enter the full path of the directory you want to organize: ").strip()
organize_files_by_extension(organizePath)
print("\nOrganization complete!")

