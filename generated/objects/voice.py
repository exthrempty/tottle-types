import typing

import pydantic


class Voice(pydantic.BaseModel):
    """
    This object represents a voice note.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param duration: Duration of the audio in seconds as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size
    """
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    duration: typing.Optional[int] = None
    mime_type: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    
    