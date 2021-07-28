import pydantic



class MessageId(pydantic.BaseModel):
    """
    This object represents a unique message identifier.
    :param message_id: Unique message identifier
    """
    
    message_id: typing.Optional[int] = None
    
    

