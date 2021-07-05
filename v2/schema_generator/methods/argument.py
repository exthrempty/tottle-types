from typing import Optional, List, Any

from humps import decamelize, depascalize, pascalize
from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from v2.schema_generator.any_of import AnyOf
from v2.schema_generator.array import Array
from v2.schema_generator.utils.wrap import wrapped


class Argument(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    default: Optional[Any] = None
    min: Optional[int] = None
    max: Optional[int] = None
    type: Optional[CustomAPITypeEnum] = None
    array: Optional[Array] = None
    any_of: Optional[List[AnyOf]] = None
    reference: Optional[str] = None

    def get_import(self) -> str:
        return f"from v2.objects.{depascalize(self.reference)} import {pascalize(self.reference)}"

    def render(self) -> str:
        """
        Renders argument as it should appear in the head of the method.
        :return: str
        """
        if self.required is True:
            return (
                f"{self.name}: typing.Optional[{self.to_pythonic_value()}]"
                f"{f' = {self.default!r}' if self.default else ' = None'}"
            )
        return f"{self.name}: {self.to_pythonic_value()}"

    def generate_summary(self) -> str:
        """
        Generates summary about this argument in Python docstring format.
        :return: str
        """
        return f":param {decamelize(self.name)}: {wrapped(self.description)}"

    def to_pythonic_value(self) -> str:
        """
        Converts type of this argument to its Python equivalent.
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
