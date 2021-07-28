import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent
from generated.objects.message_entity import MessageEntity


class InlineQueryResultDocument(pydantic.BaseModel):
    """
    Represents a link to a file. By default, this file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the file. Currently, only .PDF and .ZIP files
    can be sent using this method.
    :param type: Type of the result, must be document
    :param id: Unique identifier for this result, 1-64 bytes
    :param title: Title for the result
    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options
    for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param document_url: A valid URL for the file
    :param mime_type: Mime type of the content of the file, either “application/pdf” or “application/zip”
    :param description: Optional. Short description of the result
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the file
    :param thumb_url: Optional. URL of the thumbnail (jpeg only) for the file
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    document_url: typing.Optional[str] = None
    mime_type: typing.Optional[str] = None
    description: typing.Optional[str] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    thumb_url: typing.Optional[str] = None
    thumb_width: typing.Optional[int] = None
    thumb_height: typing.Optional[int] = None
    
    