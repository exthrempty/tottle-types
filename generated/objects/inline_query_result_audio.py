import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent
from generated.objects.message_entity import MessageEntity


class InlineQueryResultAudio(pydantic.BaseModel):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the audio.
    :param type: Type of the result, must be audio
    :param id: Unique identifier for this result, 1-64 bytes
    :param audio_url: A valid URL for the audio file
    :param title: Title
    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param performer: Optional. Performer
    :param audio_duration: Optional. Audio duration in seconds
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    audio_url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    performer: typing.Optional[str] = None
    audio_duration: typing.Optional[int] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    
    