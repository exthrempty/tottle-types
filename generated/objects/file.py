import typing

import pydantic


class File(pydantic.BaseModel):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via
    the link https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt;. It is
    guaranteed that the link will be valid for at least 1 hour. When the link expires, a
    new one can be requested by calling getFile. Maximum file size to download is 20 MB
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param file_size: Optional. File size, if known
    :param file_path: Optional. File path. Use
    https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt; to get the file.
    """
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    file_path: typing.Optional[str] = None
    
    