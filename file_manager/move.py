import os
import shutil

def move_files(source, destination):
    """Move files from source to destination folder."""
    if not os.path.exists(source):
        print(f" Source folder not found: {source}")
        return

    os.makedirs(destination, exist_ok=True)

    for filename in os.listdir(source):
        src_path = os.path.join(source, filename)
        if os.path.isfile(src_path):
            dst_path = os.path.join(destination, filename)
            shutil.move(src_path, dst_path)
            print(f" Moved: {filename} → {destination}")

