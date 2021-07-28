import pydantic



class BotCommandScopeAllGroupChats(pydantic.BaseModel):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.
    :param type: Scope type, must be all_group_chats
    """
    
    type: typing.Optional[str] = None
    
    

