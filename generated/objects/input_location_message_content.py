import pydantic



class InputLocationMessageContent(pydantic.BaseModel):
    """
    Represents the content of a location message to be sent as the result of an inline
    query.
    :param latitude: Latitude of the location in degrees
    :param longitude: Longitude of the location in degrees
    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Optional. Period in seconds for which the location can be updated, should be between
    60 and 86400.
    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees.
    Must be between 1 and 360 if specified.
    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about
    approaching another chat member, in meters. Must be between 1 and 100000 if
    specified.
    """
    
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    horizontal_accuracy: typing.Optional[float] = None
    live_period: typing.Optional[int] = None
    heading: typing.Optional[int] = None
    proximity_alert_radius: typing.Optional[int] = None
    
    

