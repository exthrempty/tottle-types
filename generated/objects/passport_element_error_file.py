import pydantic



class PassportElementErrorFile(pydantic.BaseModel):
    """
    Represents an issue with a document scan. The error is considered resolved when the
    file with the document scan changes.
    :param source: Error source, must be file
    :param type: The section of the user's Telegram Passport which has the issue, one of
    “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hash: Base64-encoded file hash
    :param message: Error message
    """
    
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    

