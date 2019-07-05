import shutil
from pathlib import Path
from typing import BinaryIO, Union
from urllib.request import urlopen


def copy(src: 'Union[BinaryIO, Path]', dest: 'Path') -> 'Path':
    """
    Copy a file or a file-like object to a specified location on the file
    system.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(src, Path):
        shutil.copyfile(str(src), str(dest))
    else:
        with dest.open('wb') as dest_file:
            shutil.copyfileobj(src, dest_file)
    return dest


def download(url: 'str', path: 'Path', force: 'bool' = False) -> 'Path':
    """
    Download a file from a URL, possibly creating intermediate directories.
    But if a file at the specified path already exists, do nothing.
    """
    if path.exists() and not force:
        return path

    with urlopen(url) as response:
         path.parent.mkdir(parents=True, exist_ok=True)
         with path.open('wb') as f:
             shutil.copyfileobj(response, f)
    return path


def remainder(s: str, prefix: str) -> 'Optional[str]':
    """
    If ``s`` startswith ``prefix``, return the rest of the string ``s``;
    otherwise return None.
    """
    if s.startswith(prefix):
        return s[len(prefix):]
    else:
        return None
