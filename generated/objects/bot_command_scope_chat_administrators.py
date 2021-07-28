import typing

import pydantic



class BotCommandScopeChatAdministrators(pydantic.BaseModel):
    """
    Represents the scope of bot commands, covering all administrators of a specific
    group or supergroup chat.
    :param type: Scope type, must be chat_administrators
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the
    format @supergroupusername)
    """
    
    type: typing.Optional[str] = None
    chat_id: typing.Optional[typing.Union[int, str]] = None
    
    

