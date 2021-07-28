import typing

import pydantic


class MessageAutoDeleteTimerChanged(pydantic.BaseModel):
    """
    This object represents a service message about a change in auto-delete timer
    settings.
    :param message_auto_delete_time: New auto-delete time for messages in the chat
    """
    message_auto_delete_time: typing.Optional[int] = None
    
    