import typing

import pydantic

from generated.objects.chat_location import ChatLocation
from generated.objects.chat_permissions import ChatPermissions
from generated.objects.chat_photo import ChatPhoto
from generated.objects.message import Message


class Chat(pydantic.BaseModel):
    """
    This object represents a chat.
    :param id: Unique identifier for this chat. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a signed 64-bit integer or double-
    precision float type are safe for storing this identifier.
    :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    :param title: Optional. Title, for supergroups, channels and group chats
    :param username: Optional. Username, for private chats, supergroups and channels if available
    :param first_name: Optional. First name of the other party in a private chat
    :param last_name: Optional. Last name of the other party in a private chat
    :param photo: Optional. Chat photo. Returned only in getChat.
    :param bio: Optional. Bio of the other party in a private chat. Returned only in getChat.
    :param description: Optional. Description, for groups, supergroups and channel chats. Returned only in
    getChat.
    :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats. Returned
    only in getChat.
    :param pinned_message: Optional. The most recent pinned message (by sending date). Returned only in
    getChat.
    :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only
    in getChat.
    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages
    sent by each unpriviledged user. Returned only in getChat.
    :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically
    deleted; in seconds. Returned only in getChat.
    :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in
    getChat.
    :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e. the discussion group
    identifier for a channel and vice versa; for supergroups and channel chats. This
    identifier may be greater than 32 bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a
    signed 64 bit integer or double-precision float type are safe for storing this
    identifier. Returned only in getChat.
    :param location: Optional. For supergroups, the location to which the supergroup is connected.
    Returned only in getChat.
    """
    id: typing.Optional[int] = None
    type: typing.Optional[str] = None
    title: typing.Optional[str] = None
    username: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    photo: typing.Optional["ChatPhoto"] = None
    bio: typing.Optional[str] = None
    description: typing.Optional[str] = None
    invite_link: typing.Optional[str] = None
    pinned_message: typing.Optional["Message"] = None
    permissions: typing.Optional["ChatPermissions"] = None
    slow_mode_delay: typing.Optional[int] = None
    message_auto_delete_time: typing.Optional[int] = None
    sticker_set_name: typing.Optional[str] = None
    can_set_sticker_set: typing.Optional[bool] = None
    linked_chat_id: typing.Optional[int] = None
    location: typing.Optional["ChatLocation"] = None
    
    