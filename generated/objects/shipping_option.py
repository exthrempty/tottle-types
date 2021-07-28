import typing

import pydantic

from generated.objects.labeled_price import LabeledPrice



class ShippingOption(pydantic.BaseModel):
    """
    This object represents one shipping option.
    :param id: Shipping option identifier
    :param title: Option title
    :param prices: List of price portions
    """
    
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    prices: typing.Optional[typing.List["LabeledPrice"]] = None
    
    

