from typing import Optional

from pydantic import BaseModel


class RecentChanges(BaseModel):
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
