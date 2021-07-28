import typing
import pydantic

from loguru import logger

from schema_generator.methods.argument import Argument
from schema_generator.methods.return_type import ReturnType


class Method(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(None)
    description: typing.Optional[str] = pydantic.Field(None)
    arguments: typing.Optional[typing.List[Argument]] = pydantic.Field(default_factory=list)
    multipart_only: typing.Optional[bool] = pydantic.Field(None)
    return_type: typing.Optional[ReturnType] = pydantic.Field(None)
    documentation_link: typing.Optional[str] = pydantic.Field(None)

    def depends(self) -> typing.Set[str]:
        import_strings_set = set()

        for argument in self.arguments:
            import_strings_set.update(argument.depends())
        import_strings_set.update(self.return_type.depends())

        logger.info("Import strings set for method {}: {}", self.name, import_strings_set)
        return import_strings_set


    # def render(self) -> str:
    #     rendered_method = RENDER_METHOD.format(
    #         name=pascalize    (self.name),
    #         endpoint=camelize(self.name),
    #         method_description=wrapped(self.description),
    #         arguments=", ".join(
    #             sorted(
    #                 (a.render() for a in self.arguments or ())
    #                 if self else (), key=lambda a: " = " in a
    #             )
    #         ),
    #         argument_description=LINE_BREAK_STYLE.join(a.generate_summary() for a in self.arguments or ()),
    #         return_type=self.return_type.to_pythonic_value(),
    #     )
    #     return rendered_method
