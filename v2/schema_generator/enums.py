from enum import Enum


class CustomAPITypeEnum(Enum):
    INTEGER = "integer"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    ARRAY = "array"
    REFERENCE = "reference"
    ANY_OF = "any_of"


TYPES_CONVERSION = {
    CustomAPITypeEnum.INTEGER: lambda: "int",
    CustomAPITypeEnum.STRING: lambda: "str",
    CustomAPITypeEnum.FLOAT: lambda: "float",
    CustomAPITypeEnum.BOOL: lambda: "bool",
    CustomAPITypeEnum.REFERENCE: lambda r: r,
    CustomAPITypeEnum.ARRAY: lambda t: "typing.List[{}]".format(t.to_pythonic_value()),
    CustomAPITypeEnum.ANY_OF: lambda l: "typing.Union[{}]".format(", ".join(t.to_pythonic_value() for t in l))
}
