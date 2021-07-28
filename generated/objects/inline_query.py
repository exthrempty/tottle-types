import pydantic

from generated.objects.location import Location
from generated.objects.user import User



class InlineQuery(pydantic.BaseModel):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.
    :param id: Unique identifier for this query
    :param from: Sender
    :param query: Text of the query (up to 256 characters)
    :param offset: Offset of the results to be returned, can be controlled by the bot
    :param chat_type: Optional. Type of the chat, from which the inline query was sent. Can be either
    “sender” for a private chat with the inline query sender, “private”, “group”,
    “supergroup”, or “channel”. The chat type should be always known for requests sent
    from official clients and most third-party clients, unless the request was sent from
    a secret chat
    :param location: Optional. Sender location, only for bots that request user location
    """
    
    id: typing.Optional[str] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    query: typing.Optional[str] = None
    offset: typing.Optional[str] = None
    chat_type: typing.Optional[str] = None
    location: typing.Optional["Location"] = None
    
    

