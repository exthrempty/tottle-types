import pydantic



class BotCommandScopeAllPrivateChats(pydantic.BaseModel):
    """
    Represents the scope of bot commands, covering all private chats.
    :param type: Scope type, must be all_private_chats
    """
    
    type: typing.Optional[str] = None
    
    

