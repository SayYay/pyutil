"""Send all files to trash which matche specific filename extension

Execute this program with directory(ies) as arguments.
Next, you will input a filename extension you want to send to trash.
Finally, all files which matches are sweeped away!
"""


""" Required modules """
# Standard
import os
import pathlib
import subprocess
import sys

# Third party
import send2trash

# Original
import pathfinder as pf


""" Function defenition """
def exit_with_wait():
    subprocess.call("PAUSE", shell=True)
    sys.exit()


def main():
    # Set current directory in case of drag & drop execution
    os.chdir(pathlib.Path(sys.argv[0]).parent)

    # Get target from arguments
    if len(sys.argv) == 1:
        target_dirs = []
        exit_with_wait()
    else:
        target_dirs = sys.argv[1:]

    # User input of filename extension
    extension = input("Input a filename extension without period -> ")

    # Find all files to discard
    target_files = []
    for dir in target_dirs:
        target_files_per_dir = pf.scan_files(dir, [extension])
        target_files += target_files_per_dir
    if not target_files:
        print("Not file found!")
        exit_with_wait()

    # Show targets and user confirmation
    for target_file in target_files:
        print("  *", target_file.name)
    confirmation = input("Are you sure to send those files to trash? [y/N] -> ")

    # Send to trash
    if str(confirmation).upper() == 'Y':
        for target_file in target_files:
            send2trash.send2trash(target_file)
        print("Done.")
    else:
        print("Cancelled.")

    exit_with_wait()


if __name__ == "__main__":
    main()