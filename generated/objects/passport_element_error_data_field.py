import pydantic



class PassportElementErrorDataField(pydantic.BaseModel):
    """
    Represents an issue in one of the data fields that was provided by the user. The
    error is considered resolved when the field's value changes.
    :param source: Error source, must be data
    :param type: The section of the user's Telegram Passport which has the error, one of
    “personal_details”, “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “address”
    :param field_name: Name of the data field which has the error
    :param data_hash: Base64-encoded data hash
    :param message: Error message
    """
    
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None
    field_name: typing.Optional[str] = None
    data_hash: typing.Optional[str] = None
    message: typing.Optional[str] = None
    
    

