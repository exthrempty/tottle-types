import typing

import pydantic

from generated.objects.user import User


class VoiceChatParticipantsInvited(pydantic.BaseModel):
    """
    This object represents a service message about new members invited to a voice chat.
    :param users: Optional. New members that were invited to the voice chat
    """
    users: typing.Optional[typing.List["User"]] = None
    
    