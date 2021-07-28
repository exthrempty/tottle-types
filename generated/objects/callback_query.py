import typing

import pydantic

from generated.objects.message import Message
from generated.objects.user import User


class CallbackQuery(pydantic.BaseModel):
    """
    This object represents an incoming callback query from a callback button in an
    inline keyboard. If the button that originated the query was attached to a message
    sent by the bot, the field message will be present. If the button was attached to a
    message sent via the bot (in inline mode), the field inline_message_id will be
    present. Exactly one of the fields data or game_short_name will be present.
    :param id: Unique identifier for this query
    :param from: Sender
    :param message: Optional. Message with the callback button that originated the query. Note that
    message content and message date will not be available if the message is too old
    :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated
    the query.
    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the
    callback button was sent. Useful for high scores in games.
    :param data: Optional. Data associated with the callback button. Be aware that a bad client can
    send arbitrary data in this field.
    :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for
    the game
    """
    id: typing.Optional[str] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    message: typing.Optional["Message"] = None
    inline_message_id: typing.Optional[str] = None
    chat_instance: typing.Optional[str] = None
    data: typing.Optional[str] = None
    game_short_name: typing.Optional[str] = None
    
    