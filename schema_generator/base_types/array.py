import typing

from humps import depascalize
from pydantic import BaseModel

from schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from schema_generator.base_types.any_of import AnyOf
from schema_generator.base_types.reference import Reference


class Array(BaseModel):
    type: typing.Optional[CustomAPITypeEnum] = None
    reference: typing.Optional[Reference] = None
    array: typing.Optional["Array"] = None
    any_of: typing.Optional[typing.List["AnyOf"]] = None

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

        if self.type == CustomAPITypeEnum.ARRAY:
            return conversion_callable(self.array)
        elif self.type == CustomAPITypeEnum.ANY_OF:
            return conversion_callable(self.any_of)
        elif self.type == CustomAPITypeEnum.REFERENCE:
            return conversion_callable(self.reference)

        return conversion_callable()


Array.update_forward_refs()
