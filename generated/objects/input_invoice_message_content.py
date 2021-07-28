import typing

import pydantic

from generated.objects.labeled_price import LabeledPrice



class InputInvoiceMessageContent(pydantic.BaseModel):
    """
    Represents the content of an invoice message to be sent as the result of an inline
    query.
    :param title: Product name, 1-32 characters
    :param description: Product description, 1-255 characters
    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
    use for your internal processes.
    :param provider_token: Payment provider token, obtained via Botfather
    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax,
    discount, delivery cost, delivery tax, bonus, etc.)
    :param max_tip_amount: Optional. The maximum accepted amount for tips in the smallest units of the currency
    (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass
    max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number
    of digits past the decimal point for each currency (2 for the majority of
    currencies). Defaults to 0
    :param suggested_tip_amounts: Optional. A JSON-serialized array of suggested amounts of tip in the smallest units
    of the currency (integer, not float/double). At most 4 suggested tip amounts can be
    specified. The suggested tip amounts must be positive, passed in a strictly
    increased order and must not exceed max_tip_amount.
    :param provider_data: Optional. A JSON-serialized object for data about the invoice, which will be shared
    with the payment provider. A detailed description of the required fields should be
    provided by the payment provider.
    :param photo_url: Optional. URL of the product photo for the invoice. Can be a photo of the goods or a
    marketing image for a service. People like it better when they see what they are
    paying for.
    :param photo_size: Optional. Photo size
    :param photo_width: Optional. Photo width
    :param photo_height: Optional. Photo height
    :param need_name: Optional. Pass True, if you require the user's full name to complete the order
    :param need_phone_number: Optional. Pass True, if you require the user's phone number to complete the order
    :param need_email: Optional. Pass True, if you require the user's email address to complete the order
    :param need_shipping_address: Optional. Pass True, if you require the user's shipping address to complete the
    order
    :param send_phone_number_to_provider: Optional. Pass True, if user's phone number should be sent to provider
    :param send_email_to_provider: Optional. Pass True, if user's email address should be sent to provider
    :param is_flexible: Optional. Pass True, if the final price depends on the shipping method
    """
    
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    payload: typing.Optional[str] = None
    provider_token: typing.Optional[str] = None
    currency: typing.Optional[str] = None
    prices: typing.Optional[typing.List["LabeledPrice"]] = None
    max_tip_amount: typing.Optional[int] = None
    suggested_tip_amounts: typing.Optional[typing.List[int]] = None
    provider_data: typing.Optional[str] = None
    photo_url: typing.Optional[str] = None
    photo_size: typing.Optional[int] = None
    photo_width: typing.Optional[int] = None
    photo_height: typing.Optional[int] = None
    need_name: typing.Optional[bool] = None
    need_phone_number: typing.Optional[bool] = None
    need_email: typing.Optional[bool] = None
    need_shipping_address: typing.Optional[bool] = None
    send_phone_number_to_provider: typing.Optional[bool] = None
    send_email_to_provider: typing.Optional[bool] = None
    is_flexible: typing.Optional[bool] = None
    
    

