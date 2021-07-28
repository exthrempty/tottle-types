import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent
from generated.objects.message_entity import MessageEntity



class InlineQueryResultPhoto(pydantic.BaseModel):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the photo.
    :param type: Type of the result, must be photo
    :param id: Unique identifier for this result, 1-64 bytes
    :param photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed
    5MB
    :param thumb_url: URL of the thumbnail for the photo
    :param photo_width: Optional. Width of the photo
    :param photo_height: Optional. Height of the photo
    :param title: Optional. Title for the result
    :param description: Optional. Short description of the result
    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    """
    
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    photo_url: typing.Optional[str] = None
    thumb_url: typing.Optional[str] = None
    photo_width: typing.Optional[int] = None
    photo_height: typing.Optional[int] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    
    

