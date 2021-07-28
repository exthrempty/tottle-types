import typing

import pydantic

from generated.objects.mask_position import MaskPosition
from generated.objects.photo_size import PhotoSize


class Sticker(pydantic.BaseModel):
    """
    This object represents a sticker.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Sticker width
    :param height: Sticker height
    :param is_animated: True, if the sticker is animated
    :param thumb: Optional. Sticker thumbnail in the .WEBP or .JPG format
    :param emoji: Optional. Emoji associated with the sticker
    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :param file_size: Optional. File size
    """
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    is_animated: typing.Optional[bool] = None
    thumb: typing.Optional["PhotoSize"] = None
    emoji: typing.Optional[str] = None
    set_name: typing.Optional[str] = None
    mask_position: typing.Optional["MaskPosition"] = None
    file_size: typing.Optional[int] = None
    
    