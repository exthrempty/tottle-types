import typing

import pydantic

from generated.objects.photo_size import PhotoSize
from generated.objects.sticker import Sticker



class StickerSet(pydantic.BaseModel):
    """
    This object represents a sticker set.
    :param name: Sticker set name
    :param title: Sticker set title
    :param is_animated: True, if the sticker set contains animated stickers
    :param contains_masks: True, if the sticker set contains masks
    :param stickers: List of all set stickers
    :param thumb: Optional. Sticker set thumbnail in the .WEBP or .TGS format
    """
    
    name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    is_animated: typing.Optional[bool] = None
    contains_masks: typing.Optional[bool] = None
    stickers: typing.Optional[typing.List["Sticker"]] = None
    thumb: typing.Optional["PhotoSize"] = None
    
    

