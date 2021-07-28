import pydantic

from generated.objects.user import User



class MessageEntity(pydantic.BaseModel):
    """
    This object represents one special entity in a text message. For example, hashtags,
    usernames, URLs, etc.
    :param type: Type of the entity. Can be “mention” (@username), “hashtag” (#hashtag), “cashtag”
    ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org), “email” (do-
    not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold text),
    “italic” (italic text), “underline” (underlined text), “strikethrough”
    (strikethrough text), “code” (monowidth string), “pre” (monowidth block),
    “text_link” (for clickable text URLs), “text_mention” (for users without usernames)
    :param offset: Offset in UTF-16 code units to the start of the entity
    :param length: Length of the entity in UTF-16 code units
    :param url: Optional. For “text_link” only, url that will be opened after user taps on the text
    :param user: Optional. For “text_mention” only, the mentioned user
    :param language: Optional. For “pre” only, the programming language of the entity text
    """
    
    type: typing.Optional[str] = None
    offset: typing.Optional[int] = None
    length: typing.Optional[int] = None
    url: typing.Optional[str] = None
    user: typing.Optional["User"] = None
    language: typing.Optional[str] = None
    
    

