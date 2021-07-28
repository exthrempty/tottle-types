import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent



class InlineQueryResultLocation(pydantic.BaseModel):
    """
    Represents a location on a map. By default, the location will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the location.
    :param type: Type of the result, must be location
    :param id: Unique identifier for this result, 1-64 Bytes
    :param latitude: Location latitude in degrees
    :param longitude: Location longitude in degrees
    :param title: Location title
    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Optional. Period in seconds for which the location can be updated, should be between
    60 and 86400.
    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees.
    Must be between 1 and 360 if specified.
    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about
    approaching another chat member, in meters. Must be between 1 and 100000 if
    specified.
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the location
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """
    
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    title: typing.Optional[str] = None
    horizontal_accuracy: typing.Optional[float] = None
    live_period: typing.Optional[int] = None
    heading: typing.Optional[int] = None
    proximity_alert_radius: typing.Optional[int] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    thumb_url: typing.Optional[str] = None
    thumb_width: typing.Optional[int] = None
    thumb_height: typing.Optional[int] = None
    
    

