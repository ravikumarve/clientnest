"""Input validation utilities for Clientnest."""
import re
from typing import Optional, Union


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def validate_email(email: str) -> bool:
    """Validate an email address.
    
    Args:
        email: The email address to validate.
        
    Returns:
        True if the email is valid, False otherwise.
        
    Raises:
        ValidationError: If the email is invalid.
    """
    if not email or not isinstance(email, str):
        raise ValidationError("Email is required")
    
    # Basic email validation regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValidationError("Invalid email format")
    
    # Check length
    if len(email) > 200:
        raise ValidationError("Email is too long")
    
    return True


def validate_password(password: str) -> bool:
    """Validate a password.
    
    Args:
        password: The password to validate.
        
    Returns:
        True if the password is valid, False otherwise.
        
    Raises:
        ValidationError: If the password is invalid.
    """
    if not password or not isinstance(password, str):
        raise ValidationError("Password is required")
    
    # Check minimum length
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    
    # Check maximum length
    if len(password) > 128:
        raise ValidationError("Password is too long")
    
    return True


def validate_name(name: str, field_name: str = "Name") -> bool:
    """Validate a name field.
    
    Args:
        name: The name to validate.
        field_name: The name of the field for error messages.
        
    Returns:
        True if the name is valid, False otherwise.
        
    Raises:
        ValidationError: If the name is invalid.
    """
    if not name or not isinstance(name, str):
        raise ValidationError(f"{field_name} is required")
    
    # Check length
    if len(name) < 2:
        raise ValidationError(f"{field_name} must be at least 2 characters long")
    
    if len(name) > 120:
        raise ValidationError(f"{field_name} is too long")
    
    # Check for valid characters (letters, spaces, hyphens, apostrophes)
    if not re.match(r'^[a-zA-Z\s\-\'\.]+$', name):
        raise ValidationError(f"{field_name} contains invalid characters")
    
    return True


def validate_slug(slug: str) -> bool:
    """Validate a URL slug.
    
    Args:
        slug: The slug to validate.
        
    Returns:
        True if the slug is valid, False otherwise.
        
    Raises:
        ValidationError: If the slug is invalid.
    """
    if not slug or not isinstance(slug, str):
        raise ValidationError("Slug is required")
    
    # Check length
    if len(slug) < 3:
        raise ValidationError("Slug must be at least 3 characters long")
    
    if len(slug) > 80:
        raise ValidationError("Slug is too long")
    
    # Check for valid characters (lowercase letters, numbers, hyphens)
    if not re.match(r'^[a-z0-9\-]+$', slug):
        raise ValidationError("Slug can only contain lowercase letters, numbers, and hyphens")
    
    # Check that it doesn't start or end with a hyphen
    if slug.startswith('-') or slug.endswith('-'):
        raise ValidationError("Slug cannot start or end with a hyphen")
    
    return True


def validate_url(url: str, allow_empty: bool = False) -> bool:
    """Validate a URL.
    
    Args:
        url: The URL to validate.
        allow_empty: Whether to allow empty URLs.
        
    Returns:
        True if the URL is valid, False otherwise.
        
    Raises:
        ValidationError: If the URL is invalid.
    """
    if not url:
        if allow_empty:
            return True
        raise ValidationError("URL is required")
    
    if not isinstance(url, str):
        raise ValidationError("URL must be a string")
    
    # Basic URL validation regex
    url_regex = r'^https?://[^\s/$.?#].[^\s]*$'
    if not re.match(url_regex, url):
        raise ValidationError("Invalid URL format")
    
    # Check length
    if len(url) > 500:
        raise ValidationError("URL is too long")
    
    return True


def validate_phone(phone: str) -> bool:
    """Validate a phone number.
    
    Args:
        phone: The phone number to validate.
        
    Returns:
        True if the phone number is valid, False otherwise.
        
    Raises:
        ValidationError: If the phone number is invalid.
    """
    if not phone or not isinstance(phone, str):
        raise ValidationError("Phone number is required")
    
    # Remove all non-numeric characters
    cleaned = re.sub(r'[^0-9]', '', phone)
    
    # Check length (10-15 digits)
    if len(cleaned) < 10 or len(cleaned) > 15:
        raise ValidationError("Invalid phone number")
    
    return True


def validate_currency(amount: Union[int, float], currency: str = "USD") -> bool:
    """Validate a currency amount.
    
    Args:
        amount: The amount to validate.
        currency: The currency code (default: USD).
        
    Returns:
        True if the amount is valid, False otherwise.
        
    Raises:
        ValidationError: If the amount is invalid.
    """
    if not isinstance(amount, (int, float)):
        raise ValidationError("Amount must be a number")
    
    if amount < 0:
        raise ValidationError("Amount cannot be negative")
    
    # Check for reasonable maximum
    if amount > 1000000:
        raise ValidationError("Amount is too large")
    
    # Validate currency code
    if not isinstance(currency, str) or len(currency) != 3:
        raise ValidationError("Invalid currency code")
    
    return True


def sanitize_string(input_string: str, max_length: int = 1000) -> str:
    """Sanitize a string input.
    
    Args:
        input_string: The string to sanitize.
        max_length: Maximum allowed length.
        
    Returns:
        The sanitized string.
        
    Raises:
        ValidationError: If the string is invalid.
    """
    if not isinstance(input_string, str):
        raise ValidationError("Input must be a string")
    
    # Remove leading/trailing whitespace
    sanitized = input_string.strip()
    
    # Check length
    if len(sanitized) > max_length:
        raise ValidationError(f"Input is too long (max {max_length} characters)")
    
    return sanitized


def validate_file_size(size: int, max_size: int = 50 * 1024 * 1024) -> bool:
    """Validate a file size.
    
    Args:
        size: The file size in bytes.
        max_size: Maximum allowed size in bytes (default: 50MB).
        
    Returns:
        True if the file size is valid, False otherwise.
        
    Raises:
        ValidationError: If the file size is invalid.
    """
    if not isinstance(size, int) or size < 0:
        raise ValidationError("Invalid file size")
    
    if size > max_size:
        raise ValidationError(f"File is too large (max {max_size / (1024 * 1024):.1f}MB)")
    
    return True


def validate_mime_type(mime_type: str, allowed_types: list[str]) -> bool:
    """Validate a MIME type.
    
    Args:
        mime_type: The MIME type to validate.
        allowed_types: List of allowed MIME types.
        
    Returns:
        True if the MIME type is valid, False otherwise.
        
    Raises:
        ValidationError: If the MIME type is invalid.
    """
    if not mime_type or not isinstance(mime_type, str):
        raise ValidationError("MIME type is required")
    
    if mime_type not in allowed_types:
        raise ValidationError(f"Invalid file type. Allowed types: {', '.join(allowed_types)}")
    
    return True
