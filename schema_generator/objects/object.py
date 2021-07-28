import typing
import pydantic

from schema_generator.objects.property import Property


class Object(pydantic.BaseModel):
    name: typing.Optional[str] = pydantic.Field(None)
    description: typing.Optional[str] = pydantic.Field(None)
    type: typing.Optional[str] = pydantic.Field(None)
    properties: typing.Optional[typing.List[Property]] = pydantic.Field(default_factory=list)
    documentation_link: typing.Optional[str] = pydantic.Field(None)

    def depends(self) -> typing.Set[str]:
        import_strings_set = set()

        for property in self.properties:
            import_strings_set.update(property.depends())

        import_strings_set.add("import pydantic")
        return import_strings_set
