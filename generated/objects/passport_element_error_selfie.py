import typing

import pydantic


class PassportElementErrorSelfie(pydantic.BaseModel):
    """
    Represents an issue with the selfie with a document. The error is considered
    resolved when the file with the selfie changes.
    :param source: Error source, must be selfie
    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”,
    “driver_license”, “identity_card”, “internal_passport”
    :param file_hash: Base64-encoded hash of the file with the selfie
    :param message: Error message
    """
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    