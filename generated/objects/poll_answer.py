import typing

import pydantic

from generated.objects.user import User


class PollAnswer(pydantic.BaseModel):
    """
    This object represents an answer of a user in a non-anonymous poll.
    :param poll_id: Unique poll identifier
    :param user: The user, who changed the answer to the poll
    :param option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user
    retracted their vote.
    """
    poll_id: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    option_ids: typing.Optional[typing.List[int]] = None
    
    