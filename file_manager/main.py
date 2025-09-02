import argparse
from rename import rename_files
from move import move_files
from cleanup import cleanup_logs

def main():
    parser = argparse.ArgumentParser(description="File Automation CLI (DevOps Style)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Rename command
    parser_rename = subparsers.add_parser("rename", help="Rename files with timestamp")
    parser_rename.add_argument("--folder", required=True, help="Folder containing files")

    # Move command
    parser_move = subparsers.add_parser("move", help="Move files between folders")
    parser_move.add_argument("--source", required=True, help="Source folder")
    parser_move.add_argument("--destination", required=True, help="Destination folder")

    # Cleanup command
    parser_cleanup = subparsers.add_parser("cleanup", help="Cleanup log files")
    parser_cleanup.add_argument("--folder", required=True, help="Log folder")
    parser_cleanup.add_argument("--size", type=int, default=1, help="Size threshold in MB (default=1)")

    args = parser.parse_args()

    if args.command == "rename":
        rename_files(args.folder)
    elif args.command == "move":
        move_files(args.source, args.destination)
    elif args.command == "cleanup":
        cleanup_logs(args.folder, args.size)

if __name__ == "__main__":
    main()

