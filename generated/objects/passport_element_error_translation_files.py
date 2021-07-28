import typing

import pydantic


class PassportElementErrorTranslationFiles(pydantic.BaseModel):
    """
    Represents an issue with the translated version of a document. The error is
    considered resolved when a file with the document translation change.
    :param source: Error source, must be translation_files
    :param type: Type of element of the user's Telegram Passport which has the issue, one of
    “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”,
    “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hashes: List of base64-encoded file hashes
    :param message: Error message
    """
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hashes: typing.Optional[typing.List[str]] = None
    message: typing.Optional[str] = None
    
    