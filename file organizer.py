import os
import shutil

# Define the target directory to organize (current working directory)
TARGET_DIR = os.getcwd()

# 1. Define the extension mapping dictionary
EXTENSION_MAP = {
    '.pdf': 'Documents',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.zip': 'Archives',
    '.py': 'Code',
    '.ipynb': 'Code'
}

def organize_directory():
    """
    Scans the directory, safely creates subfolders based on file types,
    moves matching files into them, and prints an execution summary.
    """
    # Track statistics
    files_moved_count = 0
    
    print(f"Scanning directory: {TARGET_DIR}\n")
    
    try:
        # 2. Use os.scandir() to loop through files safely
        with os.scandir(TARGET_DIR) as entries:
            for entry in entries:
                # Process only files, ignore directories and the script itself
                if entry.is_file() and entry.name != 'organizer.py':
                    file_ext = os.path.splitext(entry.name)[1].lower()
                    
                    # Check if the file extension is mapped to a folder
                    if file_ext in EXTENSION_MAP:
                        folder_name = EXTENSION_MAP[file_ext]
                        destination_folder = os.path.join(TARGET_DIR, folder_name)
                        
                        # Dynamically create the subfolder if it doesn't exist
                        if not os.path.exists(destination_folder):
                            os.makedirs(destination_folder)
                            
                        source_path = entry.path
                        destination_path = os.path.join(destination_folder, entry.name)
                        
                        # 4. Implement try-except blocks to catch FileExistsError or PermissionError
                        try:
                            # 3. Use shutil.move() to relocate files safely
                            shutil.move(source_path, destination_path)
                            print(f"[MOVED] {entry.name} -> {folder_name}/")
                            files_moved_count += 1
                        except FileExistsError:
                            print(f"[SKIPPED] File already exists at destination: {entry.name}")
                        except PermissionError:
                            print(f"[ERROR] Permission denied to move file: {entry.name}")
                        except Exception as e:
                            print(f"[ERROR] Failed to move {entry.name}: {e}")
                            
    except Exception as e:
        print(f"An error occurred while scanning the directory: {e}")
        return

    # 5. Print a formatted execution summary showing total files relocated
    print("\n" + "="*35)
    print("        EXECUTION SUMMARY        ")
    print("="*35)
    print(f"Total files successfully relocated: {files_moved_count}")
    print("="*35)

if __name__ == "_main_":
    organize_directory()