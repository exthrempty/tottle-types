import pydantic



class Location(pydantic.BaseModel):
    """
    This object represents a point on the map.
    :param longitude: Longitude as defined by sender
    :param latitude: Latitude as defined by sender
    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Optional. Time relative to the message sending date, during which the location can
    be updated, in seconds. For active live locations only.
    :param heading: Optional. The direction in which user is moving, in degrees; 1-360. For active live
    locations only.
    :param proximity_alert_radius: Optional. Maximum distance for proximity alerts about approaching another chat
    member, in meters. For sent live locations only.
    """
    
    longitude: typing.Optional[float] = None
    latitude: typing.Optional[float] = None
    horizontal_accuracy: typing.Optional[float] = None
    live_period: typing.Optional[int] = None
    heading: typing.Optional[int] = None
    proximity_alert_radius: typing.Optional[int] = None
    
    

