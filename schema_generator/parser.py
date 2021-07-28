from json import JSONDecodeError

from pydantic import ValidationError
from requests import Response, get

from schema_generator.body.body import Body


class Parser:
    @staticmethod
    def get_custom_api_schema() -> Response:
        """Gets fresh custom.json schema from ark0f.github.io"""
        response = get("https://ark0f.github.io/tg-bot-api/custom.json")
        return response

    def get_body(self) -> Body:
        try:
            response = self.get_custom_api_schema()
            schema = Body(**response.json())
        except (ValidationError, JSONDecodeError):
            raise RuntimeError("Invalid response")
        return schema
