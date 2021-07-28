import typing

import pydantic

from generated.objects.callback_query import CallbackQuery
from generated.objects.chat_member_updated import ChatMemberUpdated
from generated.objects.chosen_inline_result import ChosenInlineResult
from generated.objects.inline_query import InlineQuery
from generated.objects.message import Message
from generated.objects.poll import Poll
from generated.objects.poll_answer import PollAnswer
from generated.objects.pre_checkout_query import PreCheckoutQuery
from generated.objects.shipping_query import ShippingQuery


class Update(pydantic.BaseModel):
    """
    This object represents an incoming update. At most one of the optional parameters
    can be present in any given update.
    :param update_id: The update's unique identifier. Update identifiers start from a certain positive
    number and increase sequentially. This ID becomes especially handy if you're using
    Webhooks, since it allows you to ignore repeated updates or to restore the correct
    update sequence, should they get out of order. If there are no new updates for at
    least a week, then identifier of the next update will be chosen randomly instead of
    sequentially.
    :param message: Optional. New incoming message of any kind — text, photo, sticker, etc.
    :param edited_message: Optional. New version of a message that is known to the bot and was edited
    :param channel_post: Optional. New incoming channel post of any kind — text, photo, sticker, etc.
    :param edited_channel_post: Optional. New version of a channel post that is known to the bot and was edited
    :param inline_query: Optional. New incoming inline query
    :param chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their
    chat partner. Please see our documentation on the feedback collecting for details on
    how to enable these updates for your bot.
    :param callback_query: Optional. New incoming callback query
    :param shipping_query: Optional. New incoming shipping query. Only for invoices with flexible price
    :param pre_checkout_query: Optional. New incoming pre-checkout query. Contains full information about checkout
    :param poll: Optional. New poll state. Bots receive only updates about stopped polls and polls,
    which are sent by the bot
    :param poll_answer: Optional. A user changed their answer in a non-anonymous poll. Bots receive new
    votes only in polls that were sent by the bot itself.
    :param my_chat_member: Optional. The bot's chat member status was updated in a chat. For private chats,
    this update is received only when the bot is blocked or unblocked by the user.
    :param chat_member: Optional. A chat member's status was updated in a chat. The bot must be an
    administrator in the chat and must explicitly specify “chat_member” in the list of
    allowed_updates to receive these updates.
    """
    update_id: typing.Optional[int] = None
    message: typing.Optional["Message"] = None
    edited_message: typing.Optional["Message"] = None
    channel_post: typing.Optional["Message"] = None
    edited_channel_post: typing.Optional["Message"] = None
    inline_query: typing.Optional["InlineQuery"] = None
    chosen_inline_result: typing.Optional["ChosenInlineResult"] = None
    callback_query: typing.Optional["CallbackQuery"] = None
    shipping_query: typing.Optional["ShippingQuery"] = None
    pre_checkout_query: typing.Optional["PreCheckoutQuery"] = None
    poll: typing.Optional["Poll"] = None
    poll_answer: typing.Optional["PollAnswer"] = None
    my_chat_member: typing.Optional["ChatMemberUpdated"] = None
    chat_member: typing.Optional["ChatMemberUpdated"] = None
    
    