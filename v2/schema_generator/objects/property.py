import keyword
from typing import Optional, List

from humps import depascalize, pascalize
from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from v2.schema_generator.any_of import AnyOf
from v2.schema_generator.array import Array


class Property(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    type: Optional[CustomAPITypeEnum] = None
    array: Optional[Array] = None
    any_of: Optional[List[AnyOf]] = None
    reference: Optional[str] = None

    def get_import(self) -> str:
        return f"from v2.objects.{depascalize(self.reference)} import {pascalize(self.reference)}"

    def render(self) -> str:
        escaped_name = self.name + ('_' if self.name in keyword.kwlist else '')

        if self.required is True:
            return f"{escaped_name}: typing.Optional[{self.to_pythonic_value()}] = None"
        return f"{escaped_name}: {self.to_pythonic_value()}"

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
