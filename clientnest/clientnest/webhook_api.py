"""Webhook API for LemonSqueezy integration."""
import hmac
import hashlib
import json
from typing import Dict, Optional

from .error_handler import PaymentError
from .rate_limiter import WEBHOOK_RATE_LIMITER, check_rate_limit
from .security_logger import log_webhook_event, SecurityEvent


def validate_webhook_signature(
    payload: bytes,
    signature: str,
    webhook_secret: str,
) -> bool:
    """Validate a LemonSqueezy webhook signature.
    
    Args:
        payload: The raw webhook payload.
        signature: The signature from the X-Signature header.
        webhook_secret: The webhook secret from environment.
        
    Returns:
        True if the signature is valid, False otherwise.
    """
    if not webhook_secret:
        return False
    
    # Calculate expected signature
    expected_signature = hmac.new(
        webhook_secret.encode(),
        payload,
        hashlib.sha256,
    ).hexdigest()
    
    # Compare signatures
    return hmac.compare_digest(signature, expected_signature)


def parse_webhook_event(payload: bytes) -> Dict:
    """Parse a webhook event payload.
    
    Args:
        payload: The raw webhook payload.
        
    Returns:
        The parsed webhook event data.
        
    Raises:
        PaymentError: If the payload is invalid.
    """
    try:
        data = json.loads(payload.decode())
        
        if not isinstance(data, dict):
            raise PaymentError("Invalid webhook payload")
        
        return data
    except json.JSONDecodeError as e:
        raise PaymentError(f"Invalid JSON payload: {str(e)}")
    except Exception as e:
        raise PaymentError(f"Failed to parse webhook payload: {str(e)}")


def get_webhook_event_type(data: Dict) -> Optional[str]:
    """Get the event type from webhook data.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        The event type, or None if not found.
    """
    # LemonSqueezy webhook format
    meta = data.get("meta", {})
    event_name = meta.get("event_name")
    
    if event_name:
        return event_name
    
    # Fallback to other formats
    return data.get("event") or data.get("type")


def get_subscription_data(data: Dict) -> Dict:
    """Extract subscription data from webhook payload.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        The subscription data.
        
    Raises:
        PaymentError: If subscription data is not found.
    """
    data_obj = data.get("data", {})
    
    if not data_obj:
        raise PaymentError("No data found in webhook payload")
    
    attributes = data_obj.get("attributes", {})
    
    if not attributes:
        raise PaymentError("No attributes found in webhook data")
    
    return attributes


def get_order_data(data: Dict) -> Dict:
    """Extract order data from webhook payload.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        The order data.
        
    Raises:
        PaymentError: If order data is not found.
    """
    data_obj = data.get("data", {})
    
    if not data_obj:
        raise PaymentError("No data found in webhook payload")
    
    attributes = data_obj.get("attributes", {})
    
    if not attributes:
        raise PaymentError("No attributes found in webhook data")
    
    return attributes


def get_agency_id_from_metadata(data: Dict) -> Optional[int]:
    """Extract agency ID from webhook metadata.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        The agency ID, or None if not found.
    """
    meta = data.get("meta", {})
    custom_data = meta.get("custom_data", {})
    
    if isinstance(custom_data, dict):
        agency_id = custom_data.get("agency_id")
        if agency_id:
            try:
                return int(agency_id)
            except (ValueError, TypeError):
                pass
    
    return None


def get_invoice_id_from_metadata(data: Dict) -> Optional[int]:
    """Extract invoice ID from webhook metadata.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        The invoice ID, or None if not found.
    """
    meta = data.get("meta", {})
    custom_data = meta.get("custom_data", {})
    
    if isinstance(custom_data, dict):
        invoice_id = custom_data.get("invoice_id")
        if invoice_id:
            try:
                return int(invoice_id)
            except (ValueError, TypeError):
                pass
    
    return None


def handle_subscription_created(data: Dict) -> Dict:
    """Handle subscription_created event.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        A dictionary with subscription details.
    """
    attributes = get_subscription_data(data)
    
    return {
        "subscription_id": attributes.get("first_subscription_item", {}).get("subscription_id"),
        "product_id": attributes.get("first_subscription_item", {}).get("product_id"),
        "variant_id": attributes.get("first_subscription_item", {}).get("variant_id"),
        "status": attributes.get("status"),
        "customer_email": attributes.get("customer_email"),
        "agency_id": get_agency_id_from_metadata(data),
    }


def handle_subscription_updated(data: Dict) -> Dict:
    """Handle subscription_updated event.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        A dictionary with subscription details.
    """
    attributes = get_subscription_data(data)
    
    return {
        "subscription_id": attributes.get("first_subscription_item", {}).get("subscription_id"),
        "status": attributes.get("status"),
        "agency_id": get_agency_id_from_metadata(data),
    }


def handle_subscription_cancelled(data: Dict) -> Dict:
    """Handle subscription_cancelled event.
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        A dictionary with subscription details.
    """
    attributes = get_subscription_data(data)
    
    return {
        "subscription_id": attributes.get("first_subscription_item", {}).get("subscription_id"),
        "status": "cancelled",
        "agency_id": get_agency_id_from_metadata(data),
    }


def handle_order_created(data: Dict) -> Dict:
    """Handle order_created event (invoice payment).
    
    Args:
        data: The parsed webhook data.
        
    Returns:
        A dictionary with order details.
    """
    attributes = get_order_data(data)
    
    return {
        "order_id": attributes.get("first_order_item", {}).get("order_id"),
        "product_id": attributes.get("first_order_item", {}).get("product_id"),
        "status": attributes.get("status"),
        "total": attributes.get("total"),
        "currency": attributes.get("currency"),
        "customer_email": attributes.get("customer_email"),
        "invoice_id": get_invoice_id_from_metadata(data),
        "agency_id": get_agency_id_from_metadata(data),
    }


def process_webhook(
    payload: bytes,
    signature: str,
    webhook_secret: str,
) -> Dict:
    """Process a webhook event.
    
    Args:
        payload: The raw webhook payload.
        signature: The signature from the X-Signature header.
        webhook_secret: The webhook secret from environment.
        
    Returns:
        A dictionary with processed event data.
        
    Raises:
        PaymentError: If webhook processing fails.
    """
    # Check rate limit
    is_allowed, remaining, reset_time = check_rate_limit(WEBHOOK_RATE_LIMITER)
    
    if not is_allowed:
        log_webhook_event(
            event_type=SecurityEvent.RATE_LIMIT_EXCEEDED,
            payload_size=len(payload),
        )
        raise PaymentError("Rate limit exceeded")
    
    # Validate signature
    if not validate_webhook_signature(payload, signature, webhook_secret):
        log_webhook_event(
            event_type=SecurityEvent.WEBHOOK_VALIDATION_FAILED,
            payload_size=len(payload),
        )
        raise PaymentError("Invalid webhook signature")
    
    # Parse payload
    data = parse_webhook_event(payload)
    
    # Get event type
    event_type = get_webhook_event_type(data)
    
    if not event_type:
        raise PaymentError("No event type found in webhook payload")
    
    # Log webhook received
    log_webhook_event(
        event_type=SecurityEvent.WEBHOOK_RECEIVED,
        event_name=event_type,
        payload_size=len(payload),
    )
    
    # Process based on event type
    if event_type == "subscription_created":
        return handle_subscription_created(data)
    elif event_type == "subscription_updated":
        return handle_subscription_updated(data)
    elif event_type == "subscription_cancelled":
        return handle_subscription_cancelled(data)
    elif event_type == "order_created":
        return handle_order_created(data)
    else:
        # Unknown event type
        log_webhook_event(
            event_type=SecurityEvent.WEBHOOK_RECEIVED,
            event_name=event_type,
            payload_size=len(payload),
        )
        return {"event_type": event_type, "data": data}


def get_webhook_secret() -> Optional[str]:
    """Get the webhook secret from environment.
    
    Returns:
        The webhook secret, or None if not configured.
    """
    import os
    return os.environ.get("LEMONSQUEEZY_WEBHOOK_SECRET")
