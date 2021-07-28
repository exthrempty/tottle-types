import typing

import pydantic


class PassportElementErrorUnspecified(pydantic.BaseModel):
    """
    Represents an issue in an unspecified place. The error is considered resolved when
    new data is added.
    :param source: Error source, must be unspecified
    :param type: Type of element of the user's Telegram Passport which has the issue
    :param element_hash: Base64-encoded element hash
    :param message: Error message
    """
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    element_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    