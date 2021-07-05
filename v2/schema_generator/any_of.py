from typing import Optional, Any, List

from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum, TYPES_CONVERSION


class AnyOf(BaseModel):
    type: Optional[CustomAPITypeEnum] = None
    any_of: Optional[List["AnyOf"]] = None
    reference: Optional[str] = None
    default: Optional[Any] = None

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
