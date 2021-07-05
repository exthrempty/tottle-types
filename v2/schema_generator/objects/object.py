from typing import Optional, List, Set

from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum
from v2.schema_generator.objects.const import RENDER_OBJECT, SIGNS_OF_TYPING
from v2.schema_generator.objects.property import Property
from v2.schema_generator.utils.wrap import wrapped


class Object(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    properties: Optional[List[Property]] = None
    documentation_link: Optional[str] = None

    def get_imports(self) -> Set[str]:
        import_strings_set = set()

        for property in (self.properties or ()):
            if property.type == CustomAPITypeEnum.REFERENCE:
                import_strings_set.add(property.get_import())
            elif property.type in SIGNS_OF_TYPING or property.required is True:
                import_strings_set.add("import typing")

        import_strings_set.add("from pydantic import BaseModel")
        return set(sorted(import_strings_set))

    def render(self) -> str:
        rendered_object = RENDER_OBJECT.format(
            name=self.name,
            description=wrapped(self.description),
            properties="\n    ".join(
                (p.render() for p in self.properties)
                if self.properties else ("pass",)
            )
        )
        return rendered_object
