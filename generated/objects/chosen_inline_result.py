import typing

import pydantic

from generated.objects.location import Location
from generated.objects.user import User


class ChosenInlineResult(pydantic.BaseModel):
    """
    Represents a result of an inline query that was chosen by the user and sent to their
    chat partner.
    :param result_id: The unique identifier for the result that was chosen
    :param from: The user that chose the result
    :param location: Optional. Sender location, only for bots that require user location
    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an
    inline keyboard attached to the message. Will be also received in callback queries
    and can be used to edit the message.
    :param query: The query that was used to obtain the result
    """
    result_id: typing.Optional[str] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    location: typing.Optional["Location"] = None
    inline_message_id: typing.Optional[str] = None
    query: typing.Optional[str] = None
    
    