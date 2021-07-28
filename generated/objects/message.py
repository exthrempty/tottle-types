import typing

import pydantic

from generated.objects.animation import Animation
from generated.objects.audio import Audio
from generated.objects.chat import Chat
from generated.objects.contact import Contact
from generated.objects.dice import Dice
from generated.objects.document import Document
from generated.objects.game import Game
from generated.objects.inline_keyboard_markup import InlineKeyboardMarkup
from generated.objects.invoice import Invoice
from generated.objects.location import Location
from generated.objects.message import Message
from generated.objects.message_auto_delete_timer_changed import \
    MessageAutoDeleteTimerChanged
from generated.objects.message_entity import MessageEntity
from generated.objects.passport_data import PassportData
from generated.objects.photo_size import PhotoSize
from generated.objects.poll import Poll
from generated.objects.proximity_alert_triggered import ProximityAlertTriggered
from generated.objects.sticker import Sticker
from generated.objects.successful_payment import SuccessfulPayment
from generated.objects.user import User
from generated.objects.venue import Venue
from generated.objects.video import Video
from generated.objects.video_note import VideoNote
from generated.objects.voice import Voice
from generated.objects.voice_chat_ended import VoiceChatEnded
from generated.objects.voice_chat_participants_invited import \
    VoiceChatParticipantsInvited
from generated.objects.voice_chat_scheduled import VoiceChatScheduled
from generated.objects.voice_chat_started import VoiceChatStarted


class Message(pydantic.BaseModel):
    """
    This object represents a message.
    :param message_id: Unique message identifier inside this chat
    :param from: Optional. Sender, empty for messages sent to channels
    :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. The channel itself for
    channel messages. The supergroup itself for messages from anonymous group
    administrators. The linked channel for messages automatically forwarded to the
    discussion group
    :param date: Date the message was sent in Unix time
    :param chat: Conversation the message belongs to
    :param forward_from: Optional. For forwarded messages, sender of the original message
    :param forward_from_chat: Optional. For messages forwarded from channels or from anonymous administrators,
    information about the original sender chat
    :param forward_from_message_id: Optional. For messages forwarded from channels, identifier of the original message
    in the channel
    :param forward_signature: Optional. For messages forwarded from channels, signature of the post author if
    present
    :param forward_sender_name: Optional. Sender's name for messages forwarded from users who disallow adding a link
    to their account in forwarded messages
    :param forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
    :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this
    field will not contain further reply_to_message fields even if it itself is a reply.
    :param via_bot: Optional. Bot through which the message was sent
    :param edit_date: Optional. Date the message was last edited in Unix time
    :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
    :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title
    of an anonymous group administrator
    :param text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands,
    etc. that appear in the text
    :param animation: Optional. Message is an animation, information about the animation. For backward
    compatibility, when this field is set, the document field will also be set
    :param audio: Optional. Message is an audio file, information about the file
    :param document: Optional. Message is a general file, information about the file
    :param photo: Optional. Message is a photo, available sizes of the photo
    :param sticker: Optional. Message is a sticker, information about the sticker
    :param video: Optional. Message is a video, information about the video
    :param video_note: Optional. Message is a video note, information about the video message
    :param voice: Optional. Message is a voice message, information about the file
    :param caption: Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024
    characters
    :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot
    commands, etc. that appear in the caption
    :param contact: Optional. Message is a shared contact, information about the contact
    :param dice: Optional. Message is a dice with random value
    :param game: Optional. Message is a game, information about the game. More about games »
    :param poll: Optional. Message is a native poll, information about the poll
    :param venue: Optional. Message is a venue, information about the venue. For backward
    compatibility, when this field is set, the location field will also be set
    :param location: Optional. Message is a shared location, information about the location
    :param new_chat_members: Optional. New members that were added to the group or supergroup and information
    about them (the bot itself may be one of these members)
    :param left_chat_member: Optional. A member was removed from the group, information about them (this member
    may be the bot itself)
    :param new_chat_title: Optional. A chat title was changed to this value
    :param new_chat_photo: Optional. A chat photo was change to this value
    :param delete_chat_photo: Optional. Service message: the chat photo was deleted
    :param group_chat_created: Optional. Service message: the group has been created
    :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be
    received in a message coming through updates, because bot can't be a member of a
    supergroup when it is created. It can only be found in reply_to_message if someone
    replies to a very first message in a directly created supergroup.
    :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be
    received in a message coming through updates, because bot can't be a member of a
    channel when it is created. It can only be found in reply_to_message if someone
    replies to a very first message in a channel.
    :param message_auto_delete_timer_changed: Optional. Service message: auto-delete timer settings changed in the chat
    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier.
    This number may have more than 32 significant bits and some programming languages
    may have difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a signed 64-bit integer or double-precision float type are safe
    for storing this identifier.
    :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified
    identifier. This number may have more than 32 significant bits and some programming
    languages may have difficulty/silent defects in interpreting it. But it has at most
    52 significant bits, so a signed 64-bit integer or double-precision float type are
    safe for storing this identifier.
    :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field
    will not contain further reply_to_message fields even if it is itself a reply.
    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More
    about payments »
    :param successful_payment: Optional. Message is a service message about a successful payment, information about
    the payment. More about payments »
    :param connected_website: Optional. The domain name of the website on which the user has logged in. More about
    Telegram Login »
    :param passport_data: Optional. Telegram Passport data
    :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's proximity
    alert while sharing Live Location.
    :param voice_chat_scheduled: Optional. Service message: voice chat scheduled
    :param voice_chat_started: Optional. Service message: voice chat started
    :param voice_chat_ended: Optional. Service message: voice chat ended
    :param voice_chat_participants_invited: Optional. Service message: new participants invited to a voice chat
    :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented
    as ordinary url buttons.
    """
    message_id: typing.Optional[int] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    sender_chat: typing.Optional["Chat"] = None
    date: typing.Optional[int] = None
    chat: typing.Optional["Chat"] = None
    forward_from: typing.Optional["User"] = None
    forward_from_chat: typing.Optional["Chat"] = None
    forward_from_message_id: typing.Optional[int] = None
    forward_signature: typing.Optional[str] = None
    forward_sender_name: typing.Optional[str] = None
    forward_date: typing.Optional[int] = None
    reply_to_message: typing.Optional["Message"] = None
    via_bot: typing.Optional["User"] = None
    edit_date: typing.Optional[int] = None
    media_group_id: typing.Optional[str] = None
    author_signature: typing.Optional[str] = None
    text: typing.Optional[str] = None
    entities: typing.Optional[typing.List["MessageEntity"]] = None
    animation: typing.Optional["Animation"] = None
    audio: typing.Optional["Audio"] = None
    document: typing.Optional["Document"] = None
    photo: typing.Optional[typing.List["PhotoSize"]] = None
    sticker: typing.Optional["Sticker"] = None
    video: typing.Optional["Video"] = None
    video_note: typing.Optional["VideoNote"] = None
    voice: typing.Optional["Voice"] = None
    caption: typing.Optional[str] = None
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = None
    contact: typing.Optional["Contact"] = None
    dice: typing.Optional["Dice"] = None
    game: typing.Optional["Game"] = None
    poll: typing.Optional["Poll"] = None
    venue: typing.Optional["Venue"] = None
    location: typing.Optional["Location"] = None
    new_chat_members: typing.Optional[typing.List["User"]] = None
    left_chat_member: typing.Optional["User"] = None
    new_chat_title: typing.Optional[str] = None
    new_chat_photo: typing.Optional[typing.List["PhotoSize"]] = None
    delete_chat_photo: typing.Optional[bool] = None
    group_chat_created: typing.Optional[bool] = None
    supergroup_chat_created: typing.Optional[bool] = None
    channel_chat_created: typing.Optional[bool] = None
    message_auto_delete_timer_changed: typing.Optional["MessageAutoDeleteTimerChanged"] = None
    migrate_to_chat_id: typing.Optional[int] = None
    migrate_from_chat_id: typing.Optional[int] = None
    pinned_message: typing.Optional["Message"] = None
    invoice: typing.Optional["Invoice"] = None
    successful_payment: typing.Optional["SuccessfulPayment"] = None
    connected_website: typing.Optional[str] = None
    passport_data: typing.Optional["PassportData"] = None
    proximity_alert_triggered: typing.Optional["ProximityAlertTriggered"] = None
    voice_chat_scheduled: typing.Optional["VoiceChatScheduled"] = None
    voice_chat_started: typing.Optional["VoiceChatStarted"] = None
    voice_chat_ended: typing.Optional["VoiceChatEnded"] = None
    voice_chat_participants_invited: typing.Optional["VoiceChatParticipantsInvited"] = None
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = None
    
    