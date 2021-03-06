import typing

import pydantic


class ChatPermissions(pydantic.BaseModel):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.
    :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations
    and venues
    :param can_send_media_messages: Optional. True, if the user is allowed to send audios, documents, photos, videos,
    video notes and voice notes, implies can_send_messages
    :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages
    :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use
    inline bots, implies can_send_media_messages
    :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their messages,
    implies can_send_media_messages
    :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other
    settings. Ignored in public supergroups
    :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat
    :param can_pin_messages: Optional. True, if the user is allowed to pin messages. Ignored in public
    supergroups
    """
    can_send_messages: typing.Optional[bool] = None
    can_send_media_messages: typing.Optional[bool] = None
    can_send_polls: typing.Optional[bool] = None
    can_send_other_messages: typing.Optional[bool] = None
    can_add_web_page_previews: typing.Optional[bool] = None
    can_change_info: typing.Optional[bool] = None
    can_invite_users: typing.Optional[bool] = None
    can_pin_messages: typing.Optional[bool] = None
    
    