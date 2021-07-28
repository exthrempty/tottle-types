import typing

import pydantic


class BotCommandScopeAllChatAdministrators(pydantic.BaseModel):
    """
    Represents the scope of bot commands, covering all group and supergroup chat
    administrators.
    :param type: Scope type, must be all_chat_administrators
    """
    type: typing.Optional[str] = None
    
    