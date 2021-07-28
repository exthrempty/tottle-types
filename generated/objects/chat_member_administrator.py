import typing

import pydantic

from generated.objects.user import User


class ChatMemberAdministrator(pydantic.BaseModel):
    """
    Represents a chat member that has some additional privileges.
    :param status: The member's status in the chat, always “administrator”
    :param user: Information about the user
    :param can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
    :param is_anonymous: True, if the user's presence in the chat is hidden
    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message
    statistics in channels, see channel members, see anonymous administrators in
    supergroups and ignore slow mode. Implied by any other administrator privilege
    :param can_delete_messages: True, if the administrator can delete messages of other users
    :param can_manage_voice_chats: True, if the administrator can manage voice chats
    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own
    privileges or demote administrators that he has promoted, directly or indirectly
    (promoted by administrators that were appointed by the user)
    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin
    messages; channels only
    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :param custom_title: Optional. Custom title for this user
    """
    status: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    can_be_edited: typing.Optional[bool] = None
    is_anonymous: typing.Optional[bool] = None
    can_manage_chat: typing.Optional[bool] = None
    can_delete_messages: typing.Optional[bool] = None
    can_manage_voice_chats: typing.Optional[bool] = None
    can_restrict_members: typing.Optional[bool] = None
    can_promote_members: typing.Optional[bool] = None
    can_change_info: typing.Optional[bool] = None
    can_invite_users: typing.Optional[bool] = None
    can_post_messages: typing.Optional[bool] = None
    can_edit_messages: typing.Optional[bool] = None
    can_pin_messages: typing.Optional[bool] = None
    custom_title: typing.Optional[str] = None
    
    