import typing

import pydantic


class PassportElementErrorTranslationFile(pydantic.BaseModel):
    """
    Represents an issue with one of the files that constitute the translation of a
    document. The error is considered resolved when the file changes.
    :param source: Error source, must be translation_file
    :param type: Type of element of the user's Telegram Passport which has the issue, one of
    “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”,
    “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hash: Base64-encoded file hash
    :param message: Error message
    """
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    file_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    