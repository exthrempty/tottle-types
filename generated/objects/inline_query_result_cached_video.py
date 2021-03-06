import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent
from generated.objects.message_entity import MessageEntity


class InlineQueryResultCachedVideo(pydantic.BaseModel):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this
    video file will be sent by the user with an optional caption. Alternatively, you can
    use input_message_content to send a message with the specified content instead of
    the video.
    :param type: Type of the result, must be video
    :param id: Unique identifier for this result, 1-64 bytes
    :param video_file_id: A valid file identifier for the video file
    :param title: Title for the result
    :param description: Optional. Short description of the result
    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    video_file_id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    
    