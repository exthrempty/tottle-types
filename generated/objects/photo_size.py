import typing

import pydantic


class PhotoSize(pydantic.BaseModel):
    """
    This object represents one size of a photo or a file / sticker thumbnail.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Photo width
    :param height: Photo height
    :param file_size: Optional. File size
    """
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    file_size: typing.Optional[int] = None
    
    