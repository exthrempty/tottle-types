import typing

import pydantic

from generated.objects.photo_size import PhotoSize


class Document(pydantic.BaseModel):
    """
    This object represents a general file (as opposed to photos, voice messages and
    audio files).
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param thumb: Optional. Document thumbnail as defined by sender
    :param file_name: Optional. Original filename as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size
    """
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    thumb: typing.Optional["PhotoSize"] = None
    file_name: typing.Optional[str] = None
    mime_type: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    
    