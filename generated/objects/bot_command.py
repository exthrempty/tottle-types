import typing

import pydantic


class BotCommand(pydantic.BaseModel):
    """
    This object represents a bot command.
    :param command: Text of the command, 1-32 characters. Can contain only lowercase English letters,
    digits and underscores.
    :param description: Description of the command, 3-256 characters.
    """
    command: typing.Optional[str] = None
    description: typing.Optional[str] = None
    
    