import typing

import pydantic


class User(pydantic.BaseModel):
    """
    This object represents a Telegram user or bot.
    :param id: Unique identifier for this user or bot. This number may have more than 32
    significant bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this identifier.
    :param is_bot: True, if this user is a bot
    :param first_name: User's or bot's first name
    :param last_name: Optional. User's or bot's last name
    :param username: Optional. User's or bot's username
    :param language_code: Optional. IETF language tag of the user's language
    :param can_join_groups: Optional. True, if the bot can be invited to groups. Returned only in getMe.
    :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    :param supports_inline_queries: Optional. True, if the bot supports inline queries. Returned only in getMe.
    """
    id: typing.Optional[int] = None
    is_bot: typing.Optional[bool] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    language_code: typing.Optional[str] = None
    can_join_groups: typing.Optional[bool] = None
    can_read_all_group_messages: typing.Optional[bool] = None
    supports_inline_queries: typing.Optional[bool] = None
    
    