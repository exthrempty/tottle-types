import typing

import pydantic

from generated.objects.user import User


class ChatMemberMember(pydantic.BaseModel):
    """
    Represents a chat member that has no additional privileges or restrictions.
    :param status: The member's status in the chat, always “member”
    :param user: Information about the user
    """
    status: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    
    