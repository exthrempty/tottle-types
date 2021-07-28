import typing

import pydantic

from generated.objects.inline_keyboard_button import InlineKeyboardButton



class InlineKeyboardMarkup(pydantic.BaseModel):
    """
    This object represents an inline keyboard that appears right next to the message it
    belongs to.
    :param inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """
    
    inline_keyboard: typing.Optional[typing.List[typing.List["InlineKeyboardButton"]]] = None
    
    

