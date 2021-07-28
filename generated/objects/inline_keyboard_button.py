import typing

import pydantic

from generated.objects.callback_game import CallbackGame
from generated.objects.login_url import LoginUrl


class InlineKeyboardButton(pydantic.BaseModel):
    """
    This object represents one button of an inline keyboard. You must use exactly one of
    the optional fields.
    :param text: Label text on the button
    :param url: Optional. HTTP or tg:// url to be opened when button is pressed
    :param login_url: Optional. An HTTP URL used to automatically authorize the user. Can be used as a
    replacement for the Telegram Login Widget.
    :param callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed,
    1-64 bytes
    :param switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their
    chats, open that chat and insert the bot's username and the specified inline query
    in the input field. Can be empty, in which case just the bot's username will be
    inserted.   Note: This offers an easy way for users to start using your bot in
    inline mode when they are currently in a private chat with it. Especially useful
    when combined with switch_pm… actions – in this case the user will be automatically
    returned to the chat they switched from, skipping the chat selection screen.
    :param switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot's username and the
    specified inline query in the current chat's input field. Can be empty, in which
    case only the bot's username will be inserted.   This offers a quick way for the
    user to open your bot in inline mode in the same chat – good for selecting something
    from multiple options.
    :param callback_game: Optional. Description of the game that will be launched when the user presses the
    button.   NOTE: This type of button must always be the first button in the first
    row.
    :param pay: Optional. Specify True, to send a Pay button.   NOTE: This type of button must
    always be the first button in the first row.
    """
    text: typing.Optional[str] = None
    url: typing.Optional[str] = None
    login_url: typing.Optional["LoginUrl"] = None
    callback_data: typing.Optional[str] = None
    switch_inline_query: typing.Optional[str] = None
    switch_inline_query_current_chat: typing.Optional[str] = None
    callback_game: typing.Optional["CallbackGame"] = None
    pay: typing.Optional[bool] = None
    
    