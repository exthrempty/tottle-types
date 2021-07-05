from typing import Optional, List

from pydantic import BaseModel

from v2.schema_generator.body.recent_changes import RecentChanges
from v2.schema_generator.body.version import Version
from v2.schema_generator.methods.method import Method
from v2.schema_generator.objects.object import Object


class Body(BaseModel):
    version: Optional[Version] = None
    recent_changes: Optional[RecentChanges] = None
    methods: Optional[List[Method]] = None
    objects: Optional[List[Object]] = None
