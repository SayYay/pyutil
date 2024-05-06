"""Module for scanning paths.

This module contains functions to scan paths.

TODO: create new function to check whether dir is leaf node or not.

"""


""" Required modules """
# Standard
import glob
import pathlib


""" Function defenition """
def scan_files(
        dir: str | pathlib.WindowsPath,
        extensions: list[str],
        recursive: bool=False) -> list[pathlib.WindowsPath]:
    """Scan file paths of specific filename extensions.

    This function scans paths of file which has specific
    filename extensions in a directory, and returns those paths
    as a list.
    You can scan paths recursively if recursive=True.

    Args:
        dir(str or WindowsPath): Target directory.
        extensions(list of str): Filename extension WITHOUT PERIOD.
                                ("JPG"=OK, ".JPG"=WRONG)
        recursive(bool): Scan recursively if True. Default=False.

    Returns:
        list[WindowsPath]: List of all file paths.

    Example:
        If you want to scan CSV files in a single directory, then write like below
        import pathfinder as pf
        csv_dir = "./data/raw/"
        csv_paths = pf.scan_files(csv_dir, ["csv"])
    """

    paths_list = []
    for extension in extensions:
        if recursive:
            glob_pattern = "**/*." + str(extension)
        else:
            glob_pattern = "*." + str(extension)

        # Get file paths and merge
        dir = pathlib.Path(dir)
        paths_list += list(dir.glob(glob_pattern))

    return paths_list


def scan_dirs(
        dir: str | pathlib.WindowsPath,
        recursive: bool=False) -> list[pathlib.WindowsPath]:
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
        import pathfinder as pf
        dir_root = "./data/"
        sub_dirs = pf.scan_dirs(dir_root, True)
    """

    root_dir = pathlib.Path(dir)

    if recursive:
        dirs = [p for p in root_dir.glob("**") if p.is_dir() and not p == root_dir]
    else:
        dirs = [p for p in root_dir.glob("*") if p.is_dir()]

    return dirs


def scan_items(
        dir: str | pathlib.WindowsPath,
        extensions: list[str]=["*"],
        recursive: bool=False) -> list[pathlib.WindowsPath]:
    """Scan file and directory paths.

    This function scans paths of file and directory paths.
    You can specify filename extensions.
    You can scan paths recursively if recursive=True.

    Args:
        dir (str | pathlib.WindowsPath): Target directory.
        extensions (list[str], optional): Filename extension WITHOUT PERIOD. Defaults to None.
                                            ("JPG"=OK, ".JPG"=WRONG)
        recursive (bool, optional): Scan recursively if True. Defaults to False.

    Returns:
        list[pathlib.WindowsPath]: List of all file paths.

    Example:
        If you want to scan CSV files in a single directory, then write like below
        import pathfinder as pf
        dir_root = "./data/raw/"
        csv_paths = pf.scan_items(dir_root)
    """

    paths_dir = scan_dirs(dir, recursive)
    paths_file = scan_files(dir, extensions, recursive)

    paths_dir.extend(paths_file)

    return paths_dir
