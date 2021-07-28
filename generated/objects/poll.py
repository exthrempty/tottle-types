import typing

import pydantic

from generated.objects.message_entity import MessageEntity
from generated.objects.poll_option import PollOption


class Poll(pydantic.BaseModel):
    """
    This object contains information about a poll.
    :param id: Unique poll identifier
    :param question: Poll question, 1-300 characters
    :param options: List of poll options
    :param total_voter_count: Total number of users that voted in the poll
    :param is_closed: True, if the poll is closed
    :param is_anonymous: True, if the poll is anonymous
    :param type: Poll type, currently can be “regular” or “quiz”
    :param allows_multiple_answers: True, if the poll allows multiple answers
    :param correct_option_id: Optional. 0-based identifier of the correct answer option. Available only for polls
    in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the
    private chat with the bot.
    :param explanation: Optional. Text that is shown when a user chooses an incorrect answer or taps on the
    lamp icon in a quiz-style poll, 0-200 characters
    :param explanation_entities: Optional. Special entities like usernames, URLs, bot commands, etc. that appear in
    the explanation
    :param open_period: Optional. Amount of time in seconds the poll will be active after creation
    :param close_date: Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    """
    id: typing.Optional[str] = None
    question: typing.Optional[str] = None
    options: typing.Optional[typing.List["PollOption"]] = None
    total_voter_count: typing.Optional[int] = None
    is_closed: typing.Optional[bool] = None
    is_anonymous: typing.Optional[bool] = None
    type: typing.Optional[str] = None
    allows_multiple_answers: typing.Optional[bool] = None
    correct_option_id: typing.Optional[int] = None
    explanation: typing.Optional[str] = None
    explanation_entities: typing.Optional[typing.List["MessageEntity"]] = None
    open_period: typing.Optional[int] = None
    close_date: typing.Optional[int] = None
    
    