import typing

import pydantic

from generated.objects.location import Location


class Venue(pydantic.BaseModel):
    """
    This object represents a venue.
    :param location: Venue location. Can't be a live location
    :param title: Name of the venue
    :param address: Address of the venue
    :param foursquare_id: Optional. Foursquare identifier of the venue
    :param foursquare_type: Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”,
    “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Optional. Google Places identifier of the venue
    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    """
    location: typing.Optional["Location"] = None
    title: typing.Optional[str] = None
    address: typing.Optional[str] = None
    foursquare_id: typing.Optional[str] = None
    foursquare_type: typing.Optional[str] = None
    google_place_id: typing.Optional[str] = None
    google_place_type: typing.Optional[str] = None
    
    