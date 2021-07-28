import pydantic

from generated.objects.photo_size import PhotoSize



class Video(pydantic.BaseModel):
    """
    This object represents a video file.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Video width as defined by sender
    :param height: Video height as defined by sender
    :param duration: Duration of the video in seconds as defined by sender
    :param thumb: Optional. Video thumbnail
    :param file_name: Optional. Original filename as defined by sender
    :param mime_type: Optional. Mime type of a file as defined by sender
    :param file_size: Optional. File size
    """
    
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    duration: typing.Optional[int] = None
    thumb: typing.Optional["PhotoSize"] = None
    file_name: typing.Optional[str] = None
    mime_type: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    
    

