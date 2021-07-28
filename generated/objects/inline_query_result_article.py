import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent


class InlineQueryResultArticle(pydantic.BaseModel):
    """
    Represents a link to an article or web page.
    :param type: Type of the result, must be article
    :param id: Unique identifier for this result, 1-64 Bytes
    :param title: Title of the result
    :param input_message_content: Content of the message to be sent
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param url: Optional. URL of the result
    :param hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
    :param description: Optional. Short description of the result
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    url: typing.Optional[str] = None
    hide_url: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    thumb_url: typing.Optional[str] = None
    thumb_width: typing.Optional[int] = None
    thumb_height: typing.Optional[int] = None
    
    