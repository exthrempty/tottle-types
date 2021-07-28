import typing
import isort


def sort_imports(code: str) -> typing.List[str]:
    return isort.code(code)
