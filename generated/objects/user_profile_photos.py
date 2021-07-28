import typing

import pydantic

from generated.objects.photo_size import PhotoSize


class UserProfilePhotos(pydantic.BaseModel):
    """
    This object represent a user's profile pictures.
    :param total_count: Total number of profile pictures the target user has
    :param photos: Requested profile pictures (in up to 4 sizes each)
    """
    total_count: typing.Optional[int] = None
    photos: typing.Optional[typing.List[typing.List["PhotoSize"]]] = None
    
    