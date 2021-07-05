import pathlib
from json import JSONDecodeError

from humps import decamelize, depascalize
from loguru import logger
from pydantic import ValidationError
from requests import get, Response

from v2.schema_generator.body.body import Body
from v2.schema_generator.utils.format import format_file


class CustomAPISchemaGenerator:
    def generate_methods(self):
        for method in self.schema.methods:
            path = pathlib.Path(".") / "methods" / f"{decamelize(method.name)}.py"

            with open(path, "w") as f:
                f.write("\n".join(method.get_imports()) + "\n\n" + method.render())

            format_file(path)
            logger.success("Method {} was successfully generated", method.name)

    def generate_objects(self):
        for object in self.schema.objects:
            path = pathlib.Path(".") / "objects" / f"{depascalize(object.name)}.py"

            with open(path, "w") as f:
                f.write("\n".join(object.get_imports()) + "\n\n" + object.render())

            format_file(path)
            logger.success("Object {} was successfully generated", object.name)

    @staticmethod
    def get_custom_api_schema() -> Response:
        """Gets fresh custom.json schema from ark0f.github.io"""
        response = get("https://ark0f.github.io/tg-bot-api/custom.json")
        return response

    @property
    def schema(self) -> Body:
        try:
            response = self.get_custom_api_schema()
            schema = Body(**response.json())
        except (ValidationError, JSONDecodeError):
            raise RuntimeError("Invalid response")
        return schema
