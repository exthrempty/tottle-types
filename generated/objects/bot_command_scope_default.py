import pydantic



class BotCommandScopeDefault(pydantic.BaseModel):
    """
    Represents the default scope of bot commands. Default commands are used if no
    commands with a narrower scope are specified for the user.
    :param type: Scope type, must be default
    """
    
    type: typing.Optional[str] = None
    
    

