import pydantic



class InputContactMessageContent(pydantic.BaseModel):
    """
    Represents the content of a contact message to be sent as the result of an inline
    query.
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Optional. Contact's last name
    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    """
    
    phone_number: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    vcard: typing.Optional[str] = None
    
    

