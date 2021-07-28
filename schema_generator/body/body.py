from typing import Optional, List

from pydantic import BaseModel

from schema_generator.body.recent_changes import RecentChanges
from schema_generator.body.version import Version
from schema_generator.methods.method import Method
from schema_generator.objects.object import Object


class Body(BaseModel):
    version: Optional[Version] = None
    recent_changes: Optional[RecentChanges] = None
    methods: Optional[List[Method]] = None
    objects: Optional[List[Object]] = None
