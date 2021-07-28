import typing

import pydantic



class PassportElementErrorFiles(pydantic.BaseModel):
    """
    Represents an issue with a list of scans. The error is considered resolved when the
    list of files containing the scans changes.
    :param source: Error source, must be files
    :param type: The section of the user's Telegram Passport which has the issue, one of
    “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hashes: List of base64-encoded file hashes
    :param message: Error message
    """
    
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hashes: typing.Optional[typing.List[str]] = None
    message: typing.Optional[str] = None
    
    

