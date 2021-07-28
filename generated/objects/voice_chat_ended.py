import typing

import pydantic


class VoiceChatEnded(pydantic.BaseModel):
    """
    This object represents a service message about a voice chat ended in the chat.
    :param duration: Voice chat duration; in seconds
    """
    duration: typing.Optional[int] = None
    
    