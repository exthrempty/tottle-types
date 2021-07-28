import pydantic

from generated.objects.photo_size import PhotoSize



class Audio(pydantic.BaseModel):
    """
    This object represents an audio file to be treated as music by the Telegram clients.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param duration: Duration of the audio in seconds as defined by sender
    :param performer: Optional. Performer of the audio as defined by sender or by audio tags
    :param title: Optional. Title of the audio as defined by sender or by audio tags
    :param file_name: Optional. Original filename as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size
    :param thumb: Optional. Thumbnail of the album cover to which the music file belongs
    """
    
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    duration: typing.Optional[int] = None
    performer: typing.Optional[str] = None
    title: typing.Optional[str] = None
    file_name: typing.Optional[str] = None
    mime_type: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    thumb: typing.Optional["PhotoSize"] = None
    
    

