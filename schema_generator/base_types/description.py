from textwrap import wrap

from pydantic import BaseModel

from schema_generator.const import LINE_BREAK_STYLE, LINE_BREAK_LENGTH


class Description(BaseModel):
    __root__: str

    def __str__(self) -> str:
        return self.__root__

    def wrapped(self) -> str:
        return LINE_BREAK_STYLE.join(
            wrap(self.__root__, LINE_BREAK_LENGTH)
        )
