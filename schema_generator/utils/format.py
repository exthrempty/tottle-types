from markdown import markdown as html
from re import sub


def to_html(string: str) -> str:
    return html(str(string))


def unmarkdown(string: str) -> str:
    html = to_html(str(string))
    return sub(r"<(.*?)>", "", html)