import os

def cleanup_logs(folder, size_mb_max=1):
    """Delete log files larger than threshold (MB)."""
    if not os.path.exists(folder):
        print(f" Log folder not found: {folder}")
        return

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if size_mb > size_mb_max:
                os.remove(file_path)
                print(f" Deleted: {filename} ")

