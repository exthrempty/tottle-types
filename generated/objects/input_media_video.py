import typing

import pydantic

from generated.objects.input_file import InputFile
from generated.objects.message_entity import MessageEntity



class InputMediaVideo(pydantic.BaseModel):
    """
    Represents a video to be sent.
    :param type: Type of the result, must be video
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the
    file is supported server-side. The thumbnail should be in JPEG format and less than
    200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the
    file is not uploaded using multipart/form-data. Thumbnails can't be reused and can
    be only uploaded as a new file, so you can pass “attach://” if the thumbnail was
    uploaded using multipart/form-data under . More info on Sending Files »
    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param width: Optional. Video width
    :param height: Optional. Video height
    :param duration: Optional. Video duration
    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    """
    
    type: typing.Optional[str] = None
    media: typing.Optional[str] = None
    thumb: typing.Optional[typing.Union["InputFile", str]] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    duration: typing.Optional[int] = None
    supports_streaming: typing.Optional[bool] = None
    
    

