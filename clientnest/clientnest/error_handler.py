"""Error handling utilities for Clientnest."""
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ClientnestError(Exception):
    """Base exception for Clientnest errors."""
    
    def __init__(self, message: str, user_message: Optional[str] = None):
        """Initialize the error.
        
        Args:
            message: Internal error message.
            user_message: User-friendly error message (optional).
        """
        super().__init__(message)
        self.message = message
        self.user_message = user_message or "An error occurred. Please try again."
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the error to a dictionary.
        
        Returns:
            A dictionary representation of the error.
        """
        return {
            "error": self.__class__.__name__,
            "message": self.user_message,
        }


class AuthenticationError(ClientnestError):
    """Exception for authentication errors."""
    
    def __init__(self, message: str = "Authentication failed"):
        """Initialize the authentication error.
        
        Args:
            message: Error message.
        """
        super().__init__(message, "Invalid email or password")


class AuthorizationError(ClientnestError):
    """Exception for authorization errors."""
    
    def __init__(self, message: str = "Access denied"):
        """Initialize the authorization error.
        
        Args:
            message: Error message.
        """
        super().__init__(message, "You don't have permission to perform this action")


class ValidationError(ClientnestError):
    """Exception for validation errors."""
    
    def __init__(self, message: str, field: Optional[str] = None):
        """Initialize the validation error.
        
        Args:
            message: Error message.
            field: Field that caused the error (optional).
        """
        super().__init__(message, message)
        self.field = field
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the error to a dictionary.
        
        Returns:
            A dictionary representation of the error.
        """
        result = super().to_dict()
        if self.field:
            result["field"] = self.field
        return result


class NotFoundError(ClientnestError):
    """Exception for not found errors."""
    
    def __init__(self, message: str = "Resource not found"):
        """Initialize the not found error.
        
        Args:
            message: Error message.
        """
        super().__init__(message, "The requested resource was not found")


class RateLimitError(ClientnestError):
    """Exception for rate limit errors."""
    
    def __init__(self, message: str = "Rate limit exceeded", retry_after: Optional[int] = None):
        """Initialize the rate limit error.
        
        Args:
            message: Error message.
            retry_after: Seconds to wait before retrying (optional).
        """
        super().__init__(message, "Too many requests. Please try again later.")
        self.retry_after = retry_after
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the error to a dictionary.
        
        Returns:
            A dictionary representation of the error.
        """
        result = super().to_dict()
        if self.retry_after:
            result["retry_after"] = self.retry_after
        return result


class FileUploadError(ClientnestError):
    """Exception for file upload errors."""
    
    def __init__(self, message: str):
        """Initialize the file upload error.
        
        Args:
            message: Error message.
        """
        super().__init__(message, "Failed to upload file")


class PaymentError(ClientnestError):
    """Exception for payment errors."""
    
    def __init__(self, message: str):
        """Initialize the payment error.
        
        Args:
            message: Error message.
        """
        super().__init__(message, "Payment processing failed")


def handle_error(error: Exception, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Handle an error and return a user-friendly response.
    
    Args:
        error: The error to handle.
        context: Additional context about the error (optional).
        
    Returns:
        A dictionary with error information.
    """
    # Log the error
    logger.error(f"Error occurred: {type(error).__name__}: {str(error)}")
    
    if context:
        logger.error(f"Error context: {context}")
    
    # Handle known error types
    if isinstance(error, ClientnestError):
        return error.to_dict()
    
    # Handle unknown errors
    logger.exception("Unhandled error")
    
    return {
        "error": "InternalServerError",
        "message": "An unexpected error occurred. Please try again later.",
    }


def log_error(error: Exception, context: Optional[Dict[str, Any]] = None) -> None:
    """Log an error with context.
    
    Args:
        error: The error to log.
        context: Additional context about the error (optional).
    """
    error_type = type(error).__name__
    error_message = str(error)
    
    logger.error(f"Error: {error_type} - {error_message}")
    
    if context:
        for key, value in context.items():
            logger.error(f"  {key}: {value}")


def get_user_message(error: Exception) -> str:
    """Get a user-friendly error message.
    
    Args:
        error: The error to get a message for.
        
    Returns:
        A user-friendly error message.
    """
    if isinstance(error, ClientnestError):
        return error.user_message
    
    # Default message for unknown errors
    return "An unexpected error occurred. Please try again later."


def is_client_error(error: Exception) -> bool:
    """Check if an error is a client error (4xx).
    
    Args:
        error: The error to check.
        
    Returns:
        True if the error is a client error, False otherwise.
    """
    client_errors = (
        AuthenticationError,
        AuthorizationError,
        ValidationError,
        NotFoundError,
        RateLimitError,
    )
    
    return isinstance(error, client_errors)


def is_server_error(error: Exception) -> bool:
    """Check if an error is a server error (5xx).
    
    Args:
        error: The error to check.
        
    Returns:
        True if the error is a server error, False otherwise.
    """
    server_errors = (
        FileUploadError,
        PaymentError,
    )
    
    return isinstance(error, server_errors)
