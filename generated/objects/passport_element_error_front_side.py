import pydantic



class PassportElementErrorFrontSide(pydantic.BaseModel):
    """
    Represents an issue with the front side of a document. The error is considered
    resolved when the file with the front side of the document changes.
    :param source: Error source, must be front_side
    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”,
    “driver_license”, “identity_card”, “internal_passport”
    :param file_hash: Base64-encoded hash of the file with the front side of the document
    :param message: Error message
    """
    
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    

