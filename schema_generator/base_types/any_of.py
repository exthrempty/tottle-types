import typing

from loguru import logger
from pydantic import BaseModel

from schema_generator.base_types.reference import Reference
from schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION


class AnyOf(BaseModel):
    type: typing.Optional[CustomAPITypeEnum] = None
    array: typing.Optional["Array"] = None
    any_of: typing.Optional[typing.List["AnyOf"]] = None
    reference: typing.Optional[Reference] = None
    default: typing.Optional[typing.Any] = None

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

    def to_pythonic_value(self) -> str:
        """
        Converts custom API type to pythonic equivalent.
        :return: str
        """
        conversion_callable = TYPES_CONVERSION.get(self.type)

        if self.type == CustomAPITypeEnum.ANY_OF:
            return conversion_callable(self.any_of)
        elif self.type == CustomAPITypeEnum.REFERENCE:
            return conversion_callable(self.reference)

        return conversion_callable()
