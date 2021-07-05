from typing import List, Optional, Set

from humps import camelize, pascalize
from loguru import logger
from pydantic import BaseModel

from v2.schema_generator.enums import CustomAPITypeEnum
from v2.schema_generator.methods.argument import Argument
from v2.schema_generator.methods.const import RENDER_METHOD, LINE_BREAK_STYLE
from v2.schema_generator.methods.return_type import ReturnType
from v2.schema_generator.objects.const import SIGNS_OF_TYPING
from v2.schema_generator.utils.wrap import wrapped


class Method(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    arguments: Optional[List[Argument]] = None
    multipart_only: Optional[bool] = None
    return_type: Optional[ReturnType] = None
    documentation_link: Optional[str] = None

    def get_imports(self) -> Set[str]:
        import_strings_set = set()

        for argument in (self.arguments or ()):
            if argument.type == CustomAPITypeEnum.REFERENCE:
                import_strings_set.add(argument.get_import())
            elif (argument.required is True) or (argument.type in SIGNS_OF_TYPING):
                import_strings_set.add("import typing")

        if self.return_type.type == CustomAPITypeEnum.REFERENCE:
            import_strings_set.add(self.return_type.get_import())
        elif self.return_type.type in SIGNS_OF_TYPING:
            import_strings_set.add("import typing")

        import_strings_set.add("from v2.schema_generator.methods.base import BaseCategory")

        logger.info("Import strings set for method {}: {}", self.name, import_strings_set)
        return import_strings_set

    def render(self) -> str:
        rendered_method = RENDER_METHOD.format(
            name=pascalize(self.name),
            endpoint=camelize(self.name),
            method_description=wrapped(self.description),
            arguments=", ".join(
                sorted(
                    (a.render() for a in self.arguments or ())
                    if self else (), key=lambda a: " = " in a
                )
            ),
            argument_description=LINE_BREAK_STYLE.join(a.generate_summary() for a in self.arguments or ()),
            return_type=self.return_type.to_pythonic_value(),
        )
        return rendered_method
