import pydantic

from generated.objects.keyboard_button_poll_type import KeyboardButtonPollType



class KeyboardButton(pydantic.BaseModel):
    """
    This object represents one button of the reply keyboard. For simple text buttons
    String can be used instead of this object to specify text of the button. Optional
    fields request_contact, request_location, and request_poll are mutually exclusive.
    :param text: Text of the button. If none of the optional fields are used, it will be sent as a
    message when the button is pressed
    :param request_contact: Optional. If True, the user's phone number will be sent as a contact when the button
    is pressed. Available in private chats only
    :param request_location: Optional. If True, the user's current location will be sent when the button is
    pressed. Available in private chats only
    :param request_poll: Optional. If specified, the user will be asked to create a poll and send it to the
    bot when the button is pressed. Available in private chats only
    """
    
    text: typing.Optional[str] = None
    request_contact: typing.Optional[bool] = None
    request_location: typing.Optional[bool] = None
    request_poll: typing.Optional["KeyboardButtonPollType"] = None
    
    

