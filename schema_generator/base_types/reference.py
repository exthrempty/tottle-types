import humps
from pydantic import BaseModel


class Reference(BaseModel):
    __root__: str

    def __str__(self) -> str:
        return self.__root__

    def depends(self) -> str:
        return "from generated.objects.{} import {}".format(
            humps.depascalize(self.__root__), self.__root__
        )

    def pythonize(self) -> str:
        if humps.is_camelcase(self.__root__):
            return humps.decamelize(self.__root__)
        elif humps.is_pascalcase(self.__root__):
            return humps.depascalize(self.__root__)