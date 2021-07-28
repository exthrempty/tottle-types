import typing

import pydantic

from generated.objects.message_entity import MessageEntity



class InputTextMessageContent(pydantic.BaseModel):
    """
    Represents the content of a text message to be sent as the result of an inline
    query.
    :param message_text: Text of the message to be sent, 1-4096 characters
    :param parse_mode: Optional. Mode for parsing entities in the message text. See formatting options for
    more details.
    :param entities: Optional. List of special entities that appear in message text, which can be
    specified instead of parse_mode
    :param disable_web_page_preview: Optional. Disables link previews for links in the sent message
    """
    
    message_text: typing.Optional[str] = None
    parse_mode: typing.Optional[str] = None
    entities: typing.Optional[typing.List["MessageEntity"]] = None
    disable_web_page_preview: typing.Optional[bool] = None
    
    

