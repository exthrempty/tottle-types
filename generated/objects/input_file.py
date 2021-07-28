import pydantic



class InputFile(pydantic.BaseModel):
    """
    This object represents the contents of a file to be uploaded. Must be posted using
    multipart/form-data in the usual way that files are uploaded via the browser.
    """
    pass
    

