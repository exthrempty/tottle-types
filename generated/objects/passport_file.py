import pydantic



class PassportFile(pydantic.BaseModel):
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram
    Passport files are in JPEG format when decrypted and don't exceed 10MB.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param file_size: File size
    :param file_date: Unix time when the file was uploaded
    """
    
    file_id: typing.Optional[str] = None
    file_unique_id: typing.Optional[str] = None
    file_size: typing.Optional[int] = None
    file_date: typing.Optional[int] = None
    
    

