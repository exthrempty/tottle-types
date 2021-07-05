from typing import Optional, Union, List

from humps import decamelize

from v2.schema_generator.enums import CustomAPITypeEnum
from v2.schema_generator.methods.argument import Argument
from v2.schema_generator.objects.property import Property


def import_all_references_from(fields: Optional[Union[List[Argument], List[Property]]] = None) -> str:
    property_imports = []

    for field in fields or ():
        if field.type == CustomAPITypeEnum.REFERENCE:
            reference_name = field.reference
            decamelized_reference_name = decamelize(reference_name)
            property_imports.append(f"from v2.objects.{reference_name} import {decamelized_reference_name})")

        return "\n".join(property_imports)
    return ""
