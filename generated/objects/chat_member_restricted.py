import pydantic

from generated.objects.user import User



class ChatMemberRestricted(pydantic.BaseModel):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups
    only.
    :param status: The member's status in the chat, always “restricted”
    :param user: Information about the user
    :param is_member: True, if the user is a member of the chat at the moment of the request
    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :param can_pin_messages: True, if the user is allowed to pin messages
    :param can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    :param can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes
    and voice notes
    :param can_send_polls: True, if the user is allowed to send polls
    :param can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots
    :param can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user
    is restricted forever
    """
    
    status: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    is_member: typing.Optional[bool] = None
    can_change_info: typing.Optional[bool] = None
    can_invite_users: typing.Optional[bool] = None
    can_pin_messages: typing.Optional[bool] = None
    can_send_messages: typing.Optional[bool] = None
    can_send_media_messages: typing.Optional[bool] = None
    can_send_polls: typing.Optional[bool] = None
    can_send_other_messages: typing.Optional[bool] = None
    can_add_web_page_previews: typing.Optional[bool] = None
    until_date: typing.Optional[int] = None
    
    

