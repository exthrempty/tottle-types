from textwrap import wrap

from schema_generator.const import LINE_BREAK_STYLE, LINE_BREAK_LENGTH


def wrapped(long_string: str) -> str:
    return LINE_BREAK_STYLE.join(
        wrap(long_string, LINE_BREAK_LENGTH)
    )
