from pathlib import Path
from subprocess import check_output
from typing import Tuple


def format_file(path: Path) -> Tuple[bytes, bytes]:
    black = check_output(["black", "-q", path])
    isort = check_output(["isort", path])
    return black, isort
