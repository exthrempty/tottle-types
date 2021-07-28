import typing

import pydantic

from generated.objects.shipping_address import ShippingAddress
from generated.objects.user import User


class ShippingQuery(pydantic.BaseModel):
    """
    This object contains information about an incoming shipping query.
    :param id: Unique query identifier
    :param from: User who sent the query
    :param invoice_payload: Bot specified invoice payload
    :param shipping_address: User specified shipping address
    """
    id: typing.Optional[str] = None
    from_: typing.Optional["User"] = pydantic.Field(None, alias='from')
    invoice_payload: typing.Optional[str] = None
    shipping_address: typing.Optional["ShippingAddress"] = None
    
    