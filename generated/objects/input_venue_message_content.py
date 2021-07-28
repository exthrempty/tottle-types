import pydantic



class InputVenueMessageContent(pydantic.BaseModel):
    """
    Represents the content of a venue message to be sent as the result of an inline
    query.
    :param latitude: Latitude of the venue in degrees
    :param longitude: Longitude of the venue in degrees
    :param title: Name of the venue
    :param address: Address of the venue
    :param foursquare_id: Optional. Foursquare identifier of the venue, if known
    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Optional. Google Places identifier of the venue
    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    """
    
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    title: typing.Optional[str] = None
    address: typing.Optional[str] = None
    foursquare_id: typing.Optional[str] = None
    foursquare_type: typing.Optional[str] = None
    google_place_id: typing.Optional[str] = None
    google_place_type: typing.Optional[str] = None
    
    

