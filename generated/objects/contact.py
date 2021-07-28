import typing

import pydantic


class Contact(pydantic.BaseModel):
    """
    This object represents a phone contact.
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Optional. Contact's last name
    :param user_id: Optional. Contact's user identifier in Telegram. This number may have more than 32
    significant bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this identifier.
    :param vcard: Optional. Additional data about the contact in the form of a vCard
    """
    phone_number: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    user_id: typing.Optional[int] = None
    vcard: typing.Optional[str] = None
    
    