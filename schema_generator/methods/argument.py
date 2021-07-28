import typing

from humps import decamelize, depascalize
from pydantic import BaseModel

from schema_generator.base_types.description import Description
from schema_generator.base_types.name import Name
from schema_generator.base_types.reference import Reference
from schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from schema_generator.base_types.any_of import AnyOf
from schema_generator.base_types.array import Array
from schema_generator.utils.wrap import wrapped


class Argument(BaseModel):
    name: typing.Optional[Name] = None
    description: typing.Optional[Description] = None
    type: typing.Optional[CustomAPITypeEnum] = None
    default: typing.Optional[typing.Any] = None
    array: typing.Optional[Array] = None
    any_of: typing.Optional[typing.List[AnyOf]] = None
    reference: typing.Optional[Reference] = None
    required: typing.Optional[bool] = None
    min: typing.Optional[int] = None
    max: typing.Optional[int] = None

    def depends(self) -> typing.Set[str]:
        import_strings_set = set()

        if self.type == CustomAPITypeEnum.ARRAY:
            import_strings_set.update(self.array.depends())
        elif self.type == CustomAPITypeEnum.ANY_OF:
            for object in self.any_of:
                import_strings_set.update(object.depends())
        elif self.type == CustomAPITypeEnum.REFERENCE:
            import_strings_set.add(self.reference.depends())

        return import_strings_set

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
