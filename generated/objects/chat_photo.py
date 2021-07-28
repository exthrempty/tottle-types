import typing

import pydantic


class ChatPhoto(pydantic.BaseModel):
    """
    This object represents a chat photo.
    :param small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for
    photo download and only for as long as the photo is not changed.
    :param small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the
    same over time and for different bots. Can't be used to download or reuse the file.
    :param big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo
    download and only for as long as the photo is not changed.
    :param big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same
    over time and for different bots. Can't be used to download or reuse the file.
    """
    small_file_id: typing.Optional[str] = None
    small_file_unique_id: typing.Optional[str] = None
    big_file_id: typing.Optional[str] = None
    big_file_unique_id: typing.Optional[str] = None
    
    