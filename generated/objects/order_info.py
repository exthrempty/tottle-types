import typing

import pydantic

from generated.objects.shipping_address import ShippingAddress


class OrderInfo(pydantic.BaseModel):
    """
    This object represents information about an order.
    :param name: Optional. User name
    :param phone_number: Optional. User's phone number
    :param email: Optional. User email
    :param shipping_address: Optional. User shipping address
    """
    name: typing.Optional[str] = None
    phone_number: typing.Optional[str] = None
    email: typing.Optional[str] = None
    shipping_address: typing.Optional["ShippingAddress"] = None
    
    