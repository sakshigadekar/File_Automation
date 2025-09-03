import os
import time

def rename_files(folder):
    """Rename files by adding a timestamp."""
    if not os.path.exists(folder):
        print(f" Folder not found: {folder}")
        return

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_{timestamp}{ext}"
            new_path = os.path.join(folder, new_filename)
            os.rename(old_path, new_path)
            print(f" File has been Renamed: {filename} → {new_filename}")

