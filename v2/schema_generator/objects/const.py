from v2.schema_generator.enums import CustomAPITypeEnum

RENDER_FILE_ROOT = """
import typing

from pydantic import BaseModel
"""
RENDER_OBJECT = """
class {name}(BaseModel):
    \"\"\"
    {description}
    \"\"\"
    {properties}
"""

SIGNS_OF_TYPING = (
    CustomAPITypeEnum.ANY_OF,
    CustomAPITypeEnum.ARRAY,
)
