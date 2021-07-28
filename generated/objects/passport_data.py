import typing

import pydantic

from generated.objects.encrypted_credentials import EncryptedCredentials
from generated.objects.encrypted_passport_element import \
    EncryptedPassportElement


class PassportData(pydantic.BaseModel):
    """
    Contains information about Telegram Passport data shared with the bot by the user.
    :param data: Array with information about documents and other Telegram Passport elements that was
    shared with the bot
    :param credentials: Encrypted credentials required to decrypt the data
    """
    data: typing.Optional[typing.List["EncryptedPassportElement"]] = None
    credentials: typing.Optional["EncryptedCredentials"] = None
    
    