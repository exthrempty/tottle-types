import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent
from generated.objects.message_entity import MessageEntity



class InlineQueryResultMpeg4Gif(pydantic.BaseModel):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By
    default, this animated MPEG-4 file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the animation.
    :param type: Type of the result, must be mpeg4_gif
    :param id: Unique identifier for this result, 1-64 bytes
    :param mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB
    :param mpeg4_width: Optional. Video width
    :param mpeg4_height: Optional. Video height
    :param mpeg4_duration: Optional. Video duration
    :param thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :param thumb_mime_type: Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
    “video/mp4”. Defaults to “image/jpeg”
    :param title: Optional. Title for the result
    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more
    details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    """
    
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    mpeg4_url: typing.Optional[str] = None
    mpeg4_width: typing.Optional[int] = None
    mpeg4_height: typing.Optional[int] = None
    mpeg4_duration: typing.Optional[int] = None
    thumb_url: typing.Optional[str] = None
    thumb_mime_type: typing.Optional[str] = None
    title: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    
    

