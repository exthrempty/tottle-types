import typing

import pydantic

from generated.objects.chat import Chat
from generated.objects.chat_invite_link import ChatInviteLink
from generated.objects.chat_member import ChatMember
from generated.objects.user import User


class ChatMemberUpdated(pydantic.BaseModel):
    """
    This object represents changes in the status of a chat member.
    :param chat: Chat the user belongs to
    :param from: Performer of the action, which resulted in the change
    :param date: Date the change was done in Unix time
    :param old_chat_member: Previous information about the chat member
    :param new_chat_member: New information about the chat member
    :param invite_link: Optional. Chat invite link, which was used by the user to join the chat; for joining
    by invite link events only.
    """
    chat: typing.Optional["Chat"] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    date: typing.Optional[int] = None
    old_chat_member: typing.Optional["ChatMember"] = None
    new_chat_member: typing.Optional["ChatMember"] = None
    invite_link: typing.Optional["ChatInviteLink"] = None
    
    