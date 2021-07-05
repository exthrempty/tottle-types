from typing import Tuple

from humps import decamelize
from regex import regex


def construct_file_head(rendered_object: str) -> str:
    head = ""

    if "typing" in rendered_object:
        head += "import typing\n\n"

    head += "from pydantic import BaseModel\n"

    for line in rendered_object.splitlines():
        if import_data := get_import_data(line):
            file_name, object_name = import_data
            head += f"from v2.objects.{file_name} import {object_name}\n"

    return head + "\n"


def get_import_data(line: str) -> Tuple[str, str]:
    if match := regex.search(r"([a-z_]+): typing\.Optional\[([A-Z][A-Za-z]+)\] = None", line):
        import_object_name: str = match.groups()[1]
        import_file_name: str = decamelize(import_object_name)
        return import_file_name, import_object_name
