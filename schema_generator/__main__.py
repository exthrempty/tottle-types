import pathlib

from schema_generator.generator import Generator
from schema_generator.parser import Parser


script_path = pathlib.Path(__file__).parent
out_dir = script_path.parent


parser = Parser()
body = parser.get_body()

generator = Generator(body)
generator.generate(out_dir)
