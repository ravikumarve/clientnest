"""Security logging utilities for Clientnest."""
import logging
from datetime import datetime
from typing import Any, Dict, Optional


# Configure security logger
security_logger = logging.getLogger("clientnest.security")
security_logger.setLevel(logging.INFO)


class SecurityEvent:
    """Security event types."""
    
    # Authentication events
    LOGIN_SUCCESS = "login_success"
    LOGIN_FAILURE = "login_failure"
    LOGOUT = "logout"
    PASSWORD_CHANGE = "password_change"
    PASSWORD_RESET_REQUEST = "password_reset_request"
    
    # Authorization events
    ACCESS_DENIED = "access_denied"
    UNAUTHORIZED_ACCESS_ATTEMPT = "unauthorized_access_attempt"
    
    # CSRF events
    CSRF_TOKEN_GENERATED = "csrf_token_generated"
    CSRF_VALIDATION_FAILED = "csrf_validation_failed"
    
    # Rate limiting events
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    
    # Data events
    DATA_ACCESS = "data_access"
    DATA_MODIFICATION = "data_modification"
    DATA_DELETION = "data_deletion"
    
    # File events
    FILE_UPLOAD = "file_upload"
    FILE_DOWNLOAD = "file_download"
    FILE_DELETION = "file_deletion"
    
    # Payment events
    PAYMENT_INITIATED = "payment_initiated"
    PAYMENT_SUCCESS = "payment_success"
    PAYMENT_FAILURE = "payment_failure"
    
    # Webhook events
    WEBHOOK_RECEIVED = "webhook_received"
    WEBHOOK_VALIDATION_FAILED = "webhook_validation_failed"
    
    # Account events
    ACCOUNT_CREATED = "account_created"
    ACCOUNT_DELETED = "account_deleted"
    ACCOUNT_LOCKED = "account_locked"
    ACCOUNT_UNLOCKED = "account_unlocked"
    
    # Invitation events
    INVITE_CREATED = "invite_created"
    INVITE_ACCEPTED = "invite_accepted"
    INVITE_EXPIRED = "invite_expired"


def log_security_event(
    event_type: str,
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    ip_address: Optional[str] = None,
    user_agent: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
) -> None:
    """Log a security event.
    
    Args:
        event_type: The type of security event.
        user_id: The ID of the user (optional).
        agency_id: The ID of the agency (optional).
        ip_address: The IP address of the request (optional).
        user_agent: The user agent string (optional).
        details: Additional details about the event (optional).
    """
    timestamp = datetime.utcnow().isoformat()
    
    event_data = {
        "timestamp": timestamp,
        "event_type": event_type,
        "user_id": user_id,
        "agency_id": agency_id,
        "ip_address": ip_address,
        "user_agent": user_agent,
        "details": details or {},
    }
    
    # Log to security logger
    security_logger.info(f"Security Event: {event_type}", extra=event_data)
    
    # Also log to standard logger for visibility
    logging.info(f"Security Event: {event_type}")


def log_authentication_event(
    event_type: str,
    email: Optional[str] = None,
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    ip_address: Optional[str] = None,
    success: bool = True,
    failure_reason: Optional[str] = None,
) -> None:
    """Log an authentication event.
    
    Args:
        event_type: The type of authentication event.
        email: The email address (optional).
        user_id: The ID of the user (optional).
        agency_id: The ID of the agency (optional).
        ip_address: The IP address (optional).
        success: Whether the authentication was successful.
        failure_reason: Reason for failure (optional).
    """
    details = {
        "email": email,
        "success": success,
    }
    
    if failure_reason:
        details["failure_reason"] = failure_reason
    
    log_security_event(
        event_type=event_type,
        user_id=user_id,
        agency_id=agency_id,
        ip_address=ip_address,
        details=details,
    )


def log_authorization_event(
    event_type: str,
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    resource: Optional[str] = None,
    action: Optional[str] = None,
    ip_address: Optional[str] = None,
) -> None:
    """Log an authorization event.
    
    Args:
        event_type: The type of authorization event.
        user_id: The ID of the user (optional).
        agency_id: The ID of the agency (optional).
        resource: The resource being accessed (optional).
        action: The action being performed (optional).
        ip_address: The IP address (optional).
    """
    details = {
        "resource": resource,
        "action": action,
    }
    
    log_security_event(
        event_type=event_type,
        user_id=user_id,
        agency_id=agency_id,
        ip_address=ip_address,
        details=details,
    )


def log_data_event(
    event_type: str,
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    resource_type: Optional[str] = None,
    resource_id: Optional[int] = None,
    ip_address: Optional[str] = None,
) -> None:
    """Log a data access/modification event.
    
    Args:
        event_type: The type of data event.
        user_id: The ID of the user (optional).
        agency_id: The ID of the agency (optional).
        resource_type: The type of resource (optional).
        resource_id: The ID of the resource (optional).
        ip_address: The IP address (optional).
    """
    details = {
        "resource_type": resource_type,
        "resource_id": resource_id,
    }
    
    log_security_event(
        event_type=event_type,
        user_id=user_id,
        agency_id=agency_id,
        ip_address=ip_address,
        details=details,
    )


def log_file_event(
    event_type: str,
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    project_id: Optional[int] = None,
    filename: Optional[str] = None,
    file_size: Optional[int] = None,
    ip_address: Optional[str] = None,
) -> None:
    """Log a file event.
    
    Args:
        event_type: The type of file event.
        user_id: The ID of the user (optional).
        agency_id: The ID of the agency (optional).
        project_id: The ID of the project (optional).
        filename: The name of the file (optional).
        file_size: The size of the file (optional).
        ip_address: The IP address (optional).
    """
    details = {
        "project_id": project_id,
        "filename": filename,
        "file_size": file_size,
    }
    
    log_security_event(
        event_type=event_type,
        user_id=user_id,
        agency_id=agency_id,
        ip_address=ip_address,
        details=details,
    )


def log_payment_event(
    event_type: str,
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    invoice_id: Optional[int] = None,
    amount: Optional[float] = None,
    currency: Optional[str] = None,
    ip_address: Optional[str] = None,
) -> None:
    """Log a payment event.
    
    Args:
        event_type: The type of payment event.
        user_id: The ID of the user (optional).
        agency_id: The ID of the agency (optional).
        invoice_id: The ID of the invoice (optional).
        amount: The payment amount (optional).
        currency: The currency code (optional).
        ip_address: The IP address (optional).
    """
    details = {
        "invoice_id": invoice_id,
        "amount": amount,
        "currency": currency,
    }
    
    log_security_event(
        event_type=event_type,
        user_id=user_id,
        agency_id=agency_id,
        ip_address=ip_address,
        details=details,
    )


def log_webhook_event(
    event_type: str,
    agency_id: Optional[int] = None,
    event_name: Optional[str] = None,
    payload_size: Optional[int] = None,
    ip_address: Optional[str] = None,
) -> None:
    """Log a webhook event.
    
    Args:
        event_type: The type of webhook event.
        agency_id: The ID of the agency (optional).
        event_name: The name of the webhook event (optional).
        payload_size: The size of the payload (optional).
        ip_address: The IP address (optional).
    """
    details = {
        "event_name": event_name,
        "payload_size": payload_size,
    }
    
    log_security_event(
        event_type=event_type,
        agency_id=agency_id,
        ip_address=ip_address,
        details=details,
    )


def get_security_logs(
    user_id: Optional[int] = None,
    agency_id: Optional[int] = None,
    event_type: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    limit: int = 100,
) -> list[Dict[str, Any]]:
    """Get security logs (placeholder for future implementation).
    
    Args:
        user_id: Filter by user ID (optional).
        agency_id: Filter by agency ID (optional).
        event_type: Filter by event type (optional).
        start_date: Filter by start date (optional).
        end_date: Filter by end date (optional).
        limit: Maximum number of logs to return.
        
    Returns:
        A list of security log entries.
        
    Note:
        This is a placeholder for future implementation with a proper log storage system.
    """
    # TODO: Implement with a proper log storage system (e.g., database, log aggregation service)
    return []
