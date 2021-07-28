import pathlib
import typing

from humps import pascalize, decamelize
from jinja2 import Environment, FileSystemLoader
from loguru import logger

from schema_generator.utils.format import unmarkdown
from schema_generator.utils.imports import sort_imports
from schema_generator.utils.wrap import wrapped

templates_dir: pathlib.Path = pathlib.Path(__file__).parent / "templates"


class TemplateRenderer:
    def __init__(self):
        self.environment = Environment(
            loader=FileSystemLoader(
                searchpath=[templates_dir]
            )
        )
        self.environment.filters.update(
            {
                "pascalize": pascalize,
                "decamelize": decamelize,
                "unmarkdown": unmarkdown,
                "sort_imports": sort_imports,
                "wrapped": wrapped,
            }
        )

    def render_template(
        self, template_name: str, context: typing.Dict[str, typing.Any],
    ):
        logger.debug("Rendering template {} with context {}", template_name, context)
        code = self.environment.get_template(template_name).render(context)
        return code

