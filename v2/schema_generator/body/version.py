from typing import Optional

from pydantic import BaseModel


class Version(BaseModel):
    major: Optional[int] = None
    minor: Optional[int] = None
    patch: Optional[int] = None
