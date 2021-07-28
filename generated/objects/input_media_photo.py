import typing

import pydantic

from generated.objects.message_entity import MessageEntity



class InputMediaPhoto(pydantic.BaseModel):
    """
    Represents a photo to be sent.
    :param type: Type of the result, must be photo
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """
    
    type: typing.Optional[str] = None
    media: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    
    

