from typing import Optional, Any, List

from humps import depascalize, pascalize
from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from v2.schema_generator.methods.any_of import AnyOf
from v2.schema_generator.methods.array import Array


class ReturnType(BaseModel):
    type: Optional[CustomAPITypeEnum] = None
    default: Optional[Any] = None
    reference: Optional[str] = None
    array: Optional[Array] = None
    any_of: Optional[List[AnyOf]] = None

    def get_import(self) -> str:
        return f"from v2.objects.{depascalize(self.reference)} import {pascalize(self.reference)}"

    def to_pythonic_value(self) -> str:
        """
        Converts custom API type to pythonic equivalent.
        :return: str
        """
        conversion_callable = TYPES_CONVERSION.get(self.type)

        if self.type == CustomAPITypeEnum.ARRAY:
            return conversion_callable(self.array)
        elif self.type == CustomAPITypeEnum.ANY_OF:
            return conversion_callable(self.any_of)
        elif self.type == CustomAPITypeEnum.REFERENCE:
            return conversion_callable(self.reference)

        return conversion_callable()
