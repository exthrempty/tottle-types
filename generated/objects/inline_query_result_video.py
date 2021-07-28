import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent
from generated.objects.message_entity import MessageEntity



class InlineQueryResultVideo(pydantic.BaseModel):
    """
    Represents a link to a page containing an embedded video player or a video file. By
    default, this video file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the video. If an InlineQueryResultVideo message
    contains an embedded video (e.g., YouTube), you must replace its content using
    input_message_content.
    :param type: Type of the result, must be video
    :param id: Unique identifier for this result, 1-64 bytes
    :param video_url: A valid URL for the embedded video player or video file
    :param mime_type: Mime type of the content of video url, “text/html” or “video/mp4”
    :param thumb_url: URL of the thumbnail (jpeg only) for the video
    :param title: Title for the result
    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param video_width: Optional. Video width
    :param video_height: Optional. Video height
    :param video_duration: Optional. Video duration in seconds
    :param description: Optional. Short description of the result
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video. This field is
    required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a
    YouTube video).
    """
    
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    video_url: typing.Optional[str] = None
    mime_type: typing.Optional[str] = None
    thumb_url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    video_width: typing.Optional[int] = None
    video_height: typing.Optional[int] = None
    video_duration: typing.Optional[int] = None
    description: typing.Optional[str] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    
    

