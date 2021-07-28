import typing

import pydantic

from generated.objects.keyboard_button import KeyboardButton



class ReplyKeyboardMarkup(pydantic.BaseModel):
    """
    This object represents a custom keyboard with reply options (see Introduction to
    bots for details and examples).
    :param keyboard: Array of button rows, each represented by an Array of KeyboardButton objects
    :param resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g.,
    make the keyboard smaller if there are just two rows of buttons). Defaults to false,
    in which case the custom keyboard is always of the same height as the app's standard
    keyboard.
    :param one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. The
    keyboard will still be available, but clients will automatically display the usual
    letter-keyboard in the chat – the user can press a special button in the input field
    to see the custom keyboard again. Defaults to false.
    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the keyboard is
    active; 1-64 characters
    :param selective: Optional. Use this parameter if you want to show the keyboard to specific users
    only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if
    the bot's message is a reply (has reply_to_message_id), sender of the original
    message.   Example: A user requests to change the bot's language, bot replies to the
    request with a keyboard to select the new language. Other users in the group don't
    see the keyboard.
    """
    
    keyboard: typing.Optional[typing.List[typing.List["KeyboardButton"]]] = None
    resize_keyboard: typing.Optional[bool] = None
    one_time_keyboard: typing.Optional[bool] = None
    input_field_placeholder: typing.Optional[str] = None
    selective: typing.Optional[bool] = None
    
    

