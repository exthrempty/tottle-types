import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent



class InlineQueryResultVenue(pydantic.BaseModel):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified content
    instead of the venue.
    :param type: Type of the result, must be venue
    :param id: Unique identifier for this result, 1-64 Bytes
    :param latitude: Latitude of the venue location in degrees
    :param longitude: Longitude of the venue location in degrees
    :param title: Title of the venue
    :param address: Address of the venue
    :param foursquare_id: Optional. Foursquare identifier of the venue if known
    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Optional. Google Places identifier of the venue
    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the venue
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """
    
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    latitude: typing.Optional[float] = None
    longitude: typing.Optional[float] = None
    title: typing.Optional[str] = None
    address: typing.Optional[str] = None
    foursquare_id: typing.Optional[str] = None
    foursquare_type: typing.Optional[str] = None
    google_place_id: typing.Optional[str] = None
    google_place_type: typing.Optional[str] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    thumb_url: typing.Optional[str] = None
    thumb_width: typing.Optional[int] = None
    thumb_height: typing.Optional[int] = None
    
    

