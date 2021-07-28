import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent


class InlineQueryResultCachedSticker(pydantic.BaseModel):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this
    sticker will be sent by the user. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the sticker.
    :param type: Type of the result, must be sticker
    :param id: Unique identifier for this result, 1-64 bytes
    :param sticker_file_id: A valid file identifier of the sticker
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the sticker
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    sticker_file_id: typing.Optional[str] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    
    