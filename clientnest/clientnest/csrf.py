"""CSRF protection utilities for Clientnest."""
import hashlib
import hmac
import secrets
from typing import Optional


def generate_csrf_token() -> str:
    """Generate a secure CSRF token.
    
    Returns:
        A random 32-byte token encoded as hex.
    """
    return secrets.token_hex(32)


def validate_csrf_token(token: str, session_token: Optional[str] = None) -> bool:
    """Validate a CSRF token against the session token.
    
    Args:
        token: The CSRF token to validate.
        session_token: The token stored in the session (optional).
        
    Returns:
        True if the token is valid, False otherwise.
    """
    if not token or not session_token:
        return False
    
    # Use constant-time comparison to prevent timing attacks
    return hmac.compare_digest(token, session_token)


def get_csrf_token_from_session() -> Optional[str]:
    """Get the CSRF token from the current session.
    
    Returns:
        The CSRF token from the session, or None if not found.
    """
    # Session handling will be implemented in Reflex state
    return None


def set_csrf_token_in_session(token: str) -> None:
    """Store the CSRF token in the current session.
    
    Args:
        token: The CSRF token to store.
    """
    # Session handling will be implemented in Reflex state
    pass


def generate_csrf_input_name() -> str:
    """Generate a unique name for the CSRF input field.
    
    Returns:
        A unique name for the CSRF input field.
    """
    return "csrf_token"


def hash_csrf_token(token: str) -> str:
    """Hash a CSRF token for storage or comparison.
    
    Args:
        token: The CSRF token to hash.
        
    Returns:
        The SHA-256 hash of the token.
    """
    return hashlib.sha256(token.encode()).hexdigest()
