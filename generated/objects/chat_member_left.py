import typing

import pydantic

from generated.objects.user import User


class ChatMemberLeft(pydantic.BaseModel):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it
    themselves.
    :param status: The member's status in the chat, always “left”
    :param user: Information about the user
    """
    status: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    
    