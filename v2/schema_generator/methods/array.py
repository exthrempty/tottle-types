from typing import Optional, List

from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION
from v2.schema_generator.methods.any_of import AnyOf


class Array(BaseModel):
    type: Optional[CustomAPITypeEnum] = None
    reference: Optional[str] = None
    array: Optional["Array"] = None
    any_of: Optional[List["AnyOf"]] = None

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
