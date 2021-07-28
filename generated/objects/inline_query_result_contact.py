import typing

import pydantic

from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.input_message_content import InputMessageContent


class InlineQueryResultContact(pydantic.BaseModel):
    """
    Represents a contact with a phone number. By default, this contact will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the contact.
    :param type: Type of the result, must be contact
    :param id: Unique identifier for this result, 1-64 Bytes
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Optional. Contact's last name
    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the contact
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """
    type: typing.Optional[str] = None
    id: typing.Optional[str] = None
    phone_number: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    vcard: typing.Optional[str] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    input_message_content: typing.Optional["InputMessageContent"] = None
    thumb_url: typing.Optional[str] = None
    thumb_width: typing.Optional[int] = None
    thumb_height: typing.Optional[int] = None
    
    