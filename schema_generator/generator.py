import contextlib
import pathlib

from humps import decamelize, depascalize
from loguru import logger

from schema_generator.body.body import Body
from schema_generator.methods.method import Method
from schema_generator.objects.object import Object
from schema_generator.template import TemplateRenderer


class Generator:
    def __init__(self, body: Body):
        self.body = body
        self.render_engine = TemplateRenderer()

    def generate(self, out_dir: pathlib.Path):
        for method in self.body.methods:
            self.generate_method(method, out_dir)
        for object in self.body.objects:
            self.generate_object(object, out_dir)

    def generate_method(self, method: Method, out_dir: pathlib.Path):
        with self.open_file(out_dir / "generated" / "methods", f"{decamelize(method.name)}.py") as f:
            f.write(self.render_engine.render_template("method.py.jinja2", {"method": method}))
        logger.success("Method {} was successfully rendered", method.name)

    def generate_object(self, object: Object, out_dir: pathlib.Path):
        with self.open_file(out_dir / "generated" / "objects", f"{depascalize(object.name)}.py") as f:
            f.write(self.render_engine.render_template("object.py.jinja2", {"object": object}))
        logger.success("Object {} was successfully rendered", object.name)

    @contextlib.contextmanager
    def open_file(self, out_dir: pathlib.Path, *path):
        file_path = pathlib.Path.joinpath(out_dir, *path)
        logger.info("Opening file {}", file_path)
        with file_path.open("w") as f:
            yield f
        logger.info("Closing file {}", file_path)
