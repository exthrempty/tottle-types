import typing

import pydantic


class ForceReply(pydantic.BaseModel):
    """
    Upon receiving a message with this object, Telegram clients will display a reply
    interface to the user (act as if the user has selected the bot's message and tapped
    'Reply'). This can be extremely useful if you want to create user-friendly step-by-
    step interfaces without having to sacrifice privacy mode.
    :param force_reply: Shows reply interface to the user, as if they manually selected the bot's message
    and tapped 'Reply'
    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the reply is active;
    1-64 characters
    :param selective: Optional. Use this parameter if you want to force reply from specific users only.
    Targets: 1) users that are @mentioned in the text of the Message object; 2) if the
    bot's message is a reply (has reply_to_message_id), sender of the original message.
    """
    force_reply: typing.Optional[bool] = None
    input_field_placeholder: typing.Optional[str] = None
    selective: typing.Optional[bool] = None
    
    