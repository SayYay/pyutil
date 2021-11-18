"""Module for scanning paths.

This module contains functions to scan paths.
"""


### Required modules ###
# Standard
import glob
import pathlib


### Function defenition ###
def scan_files(dir, extension, recursive=False):
    """Scan file paths of a specific filename extension.

    This function scans paths of file which has a specific
    filename extension in a directory, and returns those paths
    as a list.
    You can scan paths recursively if recursive=True.

    Args:
        dir(str or WindowsPath): Target directory.
        extension(str): Filename extension INCLUDING PERIOD.
                        (".JPG"=OK, "JPG"=WRONG)
        recursive(bool): Scan recursively if True. Default=False.

    Returns:
        list[WindowsPath]: List of all file paths.

    Example:
        If you want to scan CSV files in a single directory,
        then write like below
        csv_dir = "./data/raw/"
        csv_paths = pf.scan_files(csv_dir, ".csv")
    """

    if recursive:
        glob_pattern = "**/*" + str(extension)
    else:
        glob_pattern = "*" + str(extension)

    path_dir = pathlib.Path(dir)
    return list(path_dir.glob(glob_pattern))


def scan_dirs(dir, recursive=False):
    """Scan paths of directories.

    This function scans subordinate directories, 
    and returns those paths as a list.
    You can scan paths recursively if recursive=True.

    Args:
        dir (str or WindowsPath): Target directory.
        recursive (bool): Scan recursively if True. Default=False.

    Returns:
        list[WindowsPath]: List of all paths.

    Example:
        If you want to scan all subordinate directories, write like below
        root_dir = "./data/"
        sub_dirs = pf.scan_directories(root_dir, True)
    """

    if recursive:
        glob_pattern = "**"
    else:
        glob_pattern = "*"

    root_dir = pathlib.Path(dir)
    return list(root_dir.glob(glob_pattern))
