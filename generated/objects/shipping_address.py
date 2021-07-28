import typing

import pydantic


class ShippingAddress(pydantic.BaseModel):
    """
    This object represents a shipping address.
    :param country_code: ISO 3166-1 alpha-2 country code
    :param state: State, if applicable
    :param city: City
    :param street_line1: First line for the address
    :param street_line2: Second line for the address
    :param post_code: Address post code
    """
    country_code: typing.Optional[str] = None
    state: typing.Optional[str] = None
    city: typing.Optional[str] = None
    street_line1: typing.Optional[str] = None
    street_line2: typing.Optional[str] = None
    post_code: typing.Optional[str] = None
    
    