#!/usr/bin/env python3
"""
Script for deleting specified path contents
"""
import os
import shutil
import argparse
from pathlib import Path

target_path = "/home/f/.cache/huggingface/lerobot/RM_Cube/Orange"

def clean_directory(path: str, remove_dir: bool = False):
    """
    Delete contents of specified path
    
    Args:
        path: Path to clean
        remove_dir: Whether to remove the directory itself
    """
    target_path = Path(path)
    
    if not target_path.exists():
        print(f"Path does not exist: {path}")
        return
    
    if target_path.is_file():
        os.remove(target_path)
        print(f"Deleted file: {path}")
    elif target_path.is_dir():
        if remove_dir:
            shutil.rmtree(target_path)
            print(f"Deleted directory and contents: {path}")
        else:
            # Only delete directory contents, keep directory
            for item in target_path.iterdir():
                if item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)
            print(f"Cleared directory contents: {path}")
    

def main():
    parser = argparse.ArgumentParser(description='Delete specified path contents')
    parser.add_argument('path', help='Path to delete')
    parser.add_argument('--remove-dir', action='store_true', 
                       help='Remove directory itself instead of just contents')
    
    args = parser.parse_args()
    
    # Confirm deletion
    print(f"About to delete: {args.path}")
    if args.remove_dir:
        print("Will delete entire directory")
    else:
        print("Will clear directory contents but keep directory")
    
    confirm = input("Confirm deletion? (y/N): ")
    if confirm.lower() in ['y', 'yes']:
        clean_directory(args.path, args.remove_dir)
    else:
        print("Operation cancelled")


if __name__ == "__main__":
    # Delete specified path directly
    print(f"Deleting path: {target_path}")
    
    confirm = input("Confirm deletion of RM_Cube directory and contents? (Y/n): ")
    if confirm.lower() in ['n', 'no']:
        print("Operation cancelled")
    else:
        clean_directory(target_path, remove_dir=True)
        
    # Can also use via command line arguments
    # main()