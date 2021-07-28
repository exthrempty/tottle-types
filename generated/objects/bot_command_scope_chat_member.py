import typing

import pydantic


class BotCommandScopeChatMember(pydantic.BaseModel):
    """
    Represents the scope of bot commands, covering a specific member of a group or
    supergroup chat.
    :param type: Scope type, must be chat_member
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the
    format @supergroupusername)
    :param user_id: Unique identifier of the target user
    """
    type: typing.Optional[str] = None
    chat_id: typing.Optional[typing.Union[int, str]] = None
    user_id: typing.Optional[int] = None
    
    