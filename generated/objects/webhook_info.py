import typing

import pydantic



class WebhookInfo(pydantic.BaseModel):
    """
    Contains information about the current status of a webhook.
    :param url: Webhook URL, may be empty if webhook is not set up
    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    :param pending_update_count: Number of updates awaiting delivery
    :param ip_address: Optional. Currently used webhook IP address
    :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver
    an update via webhook
    :param last_error_message: Optional. Error message in human-readable format for the most recent error that
    happened when trying to deliver an update via webhook
    :param max_connections: Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook
    for update delivery
    :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update
    types except chat_member
    """
    
    url: typing.Optional[str] = None
    has_custom_certificate: typing.Optional[bool] = None
    pending_update_count: typing.Optional[int] = None
    ip_address: typing.Optional[str] = None
    last_error_date: typing.Optional[int] = None
    last_error_message: typing.Optional[str] = None
    max_connections: typing.Optional[int] = None
    allowed_updates: typing.Optional[typing.List[str]] = None
    
    

