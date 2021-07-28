import pydantic

from generated.objects.user import User



class ChatMemberOwner(pydantic.BaseModel):
    """
    Represents a chat member that owns the chat and has all administrator privileges.
    :param status: The member's status in the chat, always “creator”
    :param user: Information about the user
    :param is_anonymous: True, if the user's presence in the chat is hidden
    :param custom_title: Optional. Custom title for this user
    """
    
    status: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    is_anonymous: typing.Optional[bool] = None
    custom_title: typing.Optional[str] = None
    
    

