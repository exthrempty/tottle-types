
import typing

from keyword import kwlist as prohibited_words
from loguru import logger
from pydantic import BaseModel

from schema_generator.base_types.description import Description
from schema_generator.base_types.name import Name
from schema_generator.base_types.reference import Reference
from schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from schema_generator.base_types.any_of import AnyOf
from schema_generator.base_types.array import Array


class Property(BaseModel):
    name: typing.Optional[Name] = None
    description: typing.Optional[Description] = None
    required: typing.Optional[bool] = None
    type: typing.Optional[CustomAPITypeEnum] = None
    array: typing.Optional[Array] = None
    any_of: typing.Optional[typing.List[AnyOf]] = None
    reference: typing.Optional[Reference] = None

    def depends(self) -> typing.Set[str]:
        import_strings_set = set()

        if self.type == CustomAPITypeEnum.ARRAY:
            import_strings_set.update(self.array.depends())
        elif self.type == CustomAPITypeEnum.ANY_OF:
            for object in self.any_of:
                import_strings_set.update(object.depends())
        elif self.type == CustomAPITypeEnum.REFERENCE:
            import_strings_set.add(self.reference.depends())

        import_strings_set.add("import typing")
        return import_strings_set

    def render(self) -> str:
        # Convert name to pythonic-like string
        name = self.name.pythonize()
        # Escape special keywords before render to avoid runtime errors
        if name in prohibited_words:
            return (
                f"{name + '_'}: typing.Optional[{self.to_pythonic_value()}] "
                f"= pydantic.Field(None, alias={name!r})"
            )
        # If name is not keyword, render as default
        return f"{name}: typing.Optional[{self.to_pythonic_value()}] = None"

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
