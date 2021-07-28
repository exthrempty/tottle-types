import typing

import pydantic

from generated.objects.photo_size import PhotoSize


class VideoNote(pydantic.BaseModel):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param length: Video width and height (diameter of the video message) as defined by sender
    :param duration: Duration of the video in seconds as defined by sender
    :param thumb: Optional. Video thumbnail
    :param file_size: Optional. File size
    """
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    length: typing.Optional[int] = None
    duration: typing.Optional[int] = None
    thumb: typing.Optional["PhotoSize"] = None
    file_size: typing.Optional[int] = None
    
    