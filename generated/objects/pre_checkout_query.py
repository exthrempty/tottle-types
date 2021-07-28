import typing

import pydantic

from generated.objects.order_info import OrderInfo
from generated.objects.user import User


class PreCheckoutQuery(pydantic.BaseModel):
    """
    This object contains information about an incoming pre-checkout query.
    :param id: Unique query identifier
    :param from: User who sent the query
    :param currency: Three-letter ISO 4217 currency code
    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    :param invoice_payload: Bot specified invoice payload
    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :param order_info: Optional. Order info provided by the user
    """
    id: typing.Optional[str] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    currency: typing.Optional[str] = None
    total_amount: typing.Optional[int] = None
    invoice_payload: typing.Optional[str] = None
    shipping_option_id: typing.Optional[str] = None
    order_info: typing.Optional["OrderInfo"] = None
    
    