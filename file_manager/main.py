import sys
from rename import rename_files
from move import move_files
from cleanup import cleanup_logs

def main():
    command = sys.argv[1]

    if command == "rename" and len(sys.argv) == 3:
        rename_files(sys.argv[2])
    elif command == "move" and len(sys.argv) == 4:
        move_files(sys.argv[2], sys.argv[3])
    elif command == "cleanup":
        folder = sys.argv[2]
        size = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        cleanup_logs(folder, size)
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()
