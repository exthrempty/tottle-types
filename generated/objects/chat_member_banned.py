import pydantic

from generated.objects.user import User



class ChatMemberBanned(pydantic.BaseModel):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or
    view chat messages.
    :param status: The member's status in the chat, always “kicked”
    :param user: Information about the user
    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user
    is banned forever
    """
    
    status: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    until_date: typing.Optional[int] = None
    
    

