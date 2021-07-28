import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup


class InlineQueryResultGame(pydantic.BaseModel):
    """
    Represents a Game.
    :param type: Type of the result, must be game
    :param id: Unique identifier for this result, 1-64 bytes
    :param game_short_name: Short name of the game
    :param reply_markup: Optional. Inline keyboard attached to the message
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    game_short_name: typing.Optional[str] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    
    