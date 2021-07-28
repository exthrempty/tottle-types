import pydantic

from generated.objects.user import User



class ChatInviteLink(pydantic.BaseModel):
    """
    Represents an invite link for a chat.
    :param invite_link: The invite link. If the link was created by another chat administrator, then the
    second part of the link will be replaced with “…”.
    :param creator: Creator of the link
    :param is_primary: True, if the link is primary
    :param is_revoked: True, if the link is revoked
    :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been
    expired
    :param member_limit: Optional. Maximum number of users that can be members of the chat simultaneously
    after joining the chat via this invite link; 1-99999
    """
    
    invite_link: typing.Optional[str] = None
    creator: typing.Optional["User"] = None
    is_primary: typing.Optional[bool] = None
    is_revoked: typing.Optional[bool] = None
    expire_date: typing.Optional[int] = None
    member_limit: typing.Optional[int] = None
    
    

