from pathlib import Path
from subprocess import check_output
from typing import Tuple


def sort_imports(line: str) -> str:
    black = check_output(["black", "-q", path])
    isort = check_output(["isort", path])
    return black, isort
