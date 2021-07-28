import typing

import pydantic

from generated.objects.location import Location


class ChatLocation(pydantic.BaseModel):
    """
    Represents a location to which a chat is connected.
    :param location: The location to which the supergroup is connected. Can't be a live location.
    :param address: Location address; 1-64 characters, as defined by the chat owner
    """
    location: typing.Optional["Location"] = None
    address: typing.Optional[str] = None
    
    