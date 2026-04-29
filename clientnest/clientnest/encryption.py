"""Encryption utilities for Clientnest."""
import base64
import os
from typing import Optional

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Get encryption key from environment or generate one
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY")

if ENCRYPTION_KEY:
    # Use the provided key
    _key = base64.urlsafe_b64decode(ENCRYPTION_KEY.encode())
else:
    # Generate a new key (in production, this should be stored securely)
    _key = Fernet.generate_key()
    ENCRYPTION_KEY = base64.urlsafe_b64encode(_key).decode()

_cipher = Fernet(_key)


def encrypt(data: str) -> str:
    """Encrypt a string.
    
    Args:
        data: The string to encrypt.
        
    Returns:
        The encrypted string as base64-encoded ciphertext.
        
    Raises:
        ValueError: If data is not a string.
    """
    if not isinstance(data, str):
        raise ValueError("Data must be a string")
    
    if not data:
        return ""
    
    encrypted = _cipher.encrypt(data.encode())
    return base64.urlsafe_b64encode(encrypted).decode()


def decrypt(encrypted_data: str) -> str:
    """Decrypt a string.
    
    Args:
        encrypted_data: The encrypted string to decrypt.
        
    Returns:
        The decrypted string.
        
    Raises:
        ValueError: If encrypted_data is not a string or decryption fails.
    """
    if not isinstance(encrypted_data, str):
        raise ValueError("Encrypted data must be a string")
    
    if not encrypted_data:
        return ""
    
    try:
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
        decrypted = _cipher.decrypt(encrypted_bytes)
        return decrypted.decode()
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")


def encrypt_bytes(data: bytes) -> bytes:
    """Encrypt bytes.
    
    Args:
        data: The bytes to encrypt.
        
    Returns:
        The encrypted bytes.
        
    Raises:
        ValueError: If data is not bytes.
    """
    if not isinstance(data, bytes):
        raise ValueError("Data must be bytes")
    
    if not data:
        return b""
    
    return _cipher.encrypt(data)


def decrypt_bytes(encrypted_data: bytes) -> bytes:
    """Decrypt bytes.
    
    Args:
        encrypted_data: The encrypted bytes to decrypt.
        
    Returns:
        The decrypted bytes.
        
    Raises:
        ValueError: If encrypted_data is not bytes or decryption fails.
    """
    if not isinstance(encrypted_data, bytes):
        raise ValueError("Encrypted data must be bytes")
    
    if not encrypted_data:
        return b""
    
    try:
        return _cipher.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")


def hash_password(password: str, salt: Optional[bytes] = None) -> tuple[str, bytes]:
    """Hash a password using PBKDF2.
    
    Args:
        password: The password to hash.
        salt: The salt to use (optional, will generate if not provided).
        
    Returns:
        A tuple of (hashed_password, salt).
        
    Raises:
        ValueError: If password is not a string.
    """
    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    hashed = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(hashed).decode(), salt


def verify_password(password: str, hashed_password: str, salt: bytes) -> bool:
    """Verify a password against a hash.
    
    Args:
        password: The password to verify.
        hashed_password: The hashed password to verify against.
        salt: The salt used for hashing.
        
    Returns:
        True if the password is correct, False otherwise.
        
    Raises:
        ValueError: If inputs are invalid.
    """
    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    
    if not isinstance(hashed_password, str):
        raise ValueError("Hashed password must be a string")
    
    if not isinstance(salt, bytes):
        raise ValueError("Salt must be bytes")
    
    try:
        new_hash, _ = hash_password(password, salt)
        return new_hash == hashed_password
    except Exception:
        return False


def generate_key() -> str:
    """Generate a new encryption key.
    
    Returns:
        A base64-encoded encryption key.
    """
    key = Fernet.generate_key()
    return base64.urlsafe_b64encode(key).decode()


def derive_key(password: str, salt: Optional[bytes] = None) -> tuple[str, bytes]:
    """Derive an encryption key from a password.
    
    Args:
        password: The password to derive the key from.
        salt: The salt to use (optional, will generate if not provided).
        
    Returns:
        A tuple of (derived_key, salt).
        
    Raises:
        ValueError: If password is not a string.
    """
    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key.decode(), salt


def is_encrypted(data: str) -> bool:
    """Check if a string is encrypted.
    
    Args:
        data: The string to check.
        
    Returns:
        True if the string appears to be encrypted, False otherwise.
    """
    if not isinstance(data, str) or not data:
        return False
    
    try:
        # Try to decode as base64
        decoded = base64.urlsafe_b64decode(data.encode())
        # Try to decrypt
        _cipher.decrypt(decoded)
        return True
    except Exception:
        return False
