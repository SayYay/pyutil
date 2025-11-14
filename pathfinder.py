"""Module for scanning paths.

This module contains functions to scan paths.

TODO: create new function to check whether dir is leaf node or not.

"""


""" Required modules """
# Standard
import glob
from pathlib import Path


""" Function defenition """
def scan_files(
        dir: str | Path,
        extensions: list[str],
        recursive: bool=False) -> list[Path]:
    """Scan file paths of specific filename extensions.

    This function scans paths of file which has specific
    filename extensions in a directory, and returns those paths
    as a list.
    You can scan paths recursively if recursive=True.

    Args:
        dir(str or Path): Target directory.
        extensions(list of str): Filename extension WITHOUT PERIOD.
                                ("JPG"=OK, ".JPG"=WRONG)
        recursive(bool): Scan recursively if True. Default=False.

    Returns:
        list[Path]: List of all file paths.

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
        dir = Path(dir)
        paths_list += list(dir.glob(glob_pattern))

    return paths_list


def scan_dirs(
        dir: str | Path,
        recursive: bool=False) -> list[Path]:
    """Scan paths of directories.

    This function scans subordinate directories,
    and returns those paths as a list.
    You can scan paths recursively if recursive=True.

    Args:
        dir (str or Path): Target directory.
        recursive (bool): Scan recursively if True. Default=False.

    Returns:
        list[Path]: List of all paths.

    Example:
        If you want to scan all subordinate directories, write like below
        import pathfinder as pf
        dir_root = "./data/"
        sub_dirs = pf.scan_dirs(dir_root, True)
    """

    root_dir = Path(dir)

    if recursive:
        dirs = [p for p in root_dir.glob("**") if p.is_dir() and not p == root_dir]
    else:
        dirs = [p for p in root_dir.glob("*") if p.is_dir()]

    return dirs


def scan_items(
        dir: str | Path,
        extensions: list[str]=["*"],
        recursive: bool=False) -> list[Path]:
    """Scan file and directory paths.

    This function scans paths of file and directory paths.
    You can specify filename extensions.
    You can scan paths recursively if recursive=True.

    Args:
        dir (str | Path): Target directory.
        extensions (list[str], optional): Filename extension WITHOUT PERIOD. Defaults to None.
                                            ("JPG"=OK, ".JPG"=WRONG)
        recursive (bool, optional): Scan recursively if True. Defaults to False.

    Returns:
        list[Path]: List of all file paths.

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


def is_leaf_dir(path: str | Path) -> bool:
    """Check whether the given path is a leaf directory.

    A "leaf directory" is defined as a directory that contains no
    subdirectories (files may exist).

    Args:
        path (str | Path): Path object representing the target directory.

    Returns:
        bool: True if the directory contains no subdirectories.

    Raises:
        TypeError: If the argument is not a Path object.
        ValueError: If None is supplied.
        FileNotFoundError: If the path does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    if path is None:
        raise ValueError("Path is None")

    if not isinstance(path, (str, Path)):
        raise TypeError(f"Path must be str or Path, not {type(path)}")

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")

    # Search subdirectories
    try:
        for p in path.iterdir():
            if p.is_dir():
                return False
        return True
    except PermissionError:
        raise PermissionError(f"Cannot access directory: {path}")
    except OSError as e:
        raise OSError(f"OS error while reading directory: {e}") from e


def is_empty_dir(path: str | Path) -> bool:
    """Check whether the given directory is empty.

    A directory is considered empty if it contains no files or subdirectories.

    Args:
        path (str | Path): Path to the target directory.

    Returns:
        bool: True if the directory is empty, False otherwise.

    Raises:
        ValueError: If the provided path is None.
        TypeError: If the provided path is not a string or Path object.
        FileNotFoundError: If the specified path does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    if path is None:
        raise ValueError("Path is None")

    if not isinstance(path, (str, Path)):
        raise TypeError(f"Path must be str or Path, not {type(path)}")

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")

    return not any(path.iterdir())
