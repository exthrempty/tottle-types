import typing

import pydantic


class PollOption(pydantic.BaseModel):
    """
    This object contains information about one answer option in a poll.
    :param text: Option text, 1-100 characters
    :param voter_count: Number of users that voted for this option
    """
    text: typing.Optional[str] = None
    voter_count: typing.Optional[int] = None
    
    