import typing

import pydantic


class PassportElementErrorReverseSide(pydantic.BaseModel):
    """
    Represents an issue with the reverse side of a document. The error is considered
    resolved when the file with reverse side of the document changes.
    :param source: Error source, must be reverse_side
    :param type: The section of the user's Telegram Passport which has the issue, one of
    “driver_license”, “identity_card”
    :param file_hash: Base64-encoded hash of the file with the reverse side of the document
    :param message: Error message
    """
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    