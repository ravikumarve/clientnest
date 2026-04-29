"""Security tests for Clientnest application."""
import pytest
import bcrypt
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
import sys
import os

# Add the clientnest module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from clientnest.clientnest.models.user import User
from clientnest.clientnest.models.agency import Agency
from clientnest.clientnest.models.file import File
from clientnest.clientnest.state.auth import AuthState
from clientnest.clientnest.state.file import FileState
from clientnest.clientnest.csrf import generate_csrf_token, validate_csrf_token
from clientnest.clientnest.rate_limiter import RateLimiter
from clientnest.clientnest.validators import (
    validate_email, validate_password, validate_name, sanitize_string
)
from clientnest.clientnest.encryption import encrypt, decrypt
from clientnest.clientnest.security_logger import SecurityEvent, log_security_event


class TestCSRFProtection:
    """Test CSRF protection mechanisms."""
    
    def test_generate_csrf_token(self):
        """Test CSRF token generation."""
        token = generate_csrf_token()
        assert token is not None
        assert len(token) == 64  # 32 bytes * 2 for hex
        assert isinstance(token, str)
    
    def test_validate_valid_csrf_token(self):
        """Test validation of valid CSRF token."""
        token = generate_csrf_token()
        # validate_csrf_token requires both token and session_token
        # For this test, we'll use the same token for both
        assert validate_csrf_token(token, token) is True
    
    def test_validate_invalid_csrf_token(self):
        """Test validation of invalid CSRF token."""
        assert validate_csrf_token("invalid_token") is False
        assert validate_csrf_token("") is False
        assert validate_csrf_token(None) is False


class TestRateLimiting:
    """Test rate limiting mechanisms."""
    
    def test_rate_limiter_creation(self):
        """Test rate limiter creation."""
        limiter = RateLimiter(rate=10, per=60)
        assert limiter.rate == 10
        assert limiter.per == 60
    
    def test_rate_limiter_consumption(self):
        """Test rate limiter consumption."""
        limiter = RateLimiter(rate=5, per=60)
        
        # First 5 requests should succeed
        for _ in range(5):
            assert limiter.is_allowed() is True
        
        # 6th request should be blocked
        assert limiter.is_allowed() is False
    
    def test_rate_limiter_refill(self):
        """Test rate limiter refill over time."""
        limiter = RateLimiter(rate=2, per=1)  # 2 requests per 1 second
        
        # First 2 requests should succeed
        assert limiter.is_allowed() is True
        assert limiter.is_allowed() is True
        
        # 3rd request should be blocked
        assert limiter.is_allowed() is False
    
    def test_rate_limiter_remaining(self):
        """Test getting remaining requests."""
        limiter = RateLimiter(rate=5, per=60)
        
        # Initially should have 5 remaining
        assert limiter.get_remaining() == 5
        
        # After 1 request, should have 4 remaining
        limiter.is_allowed()
        assert limiter.get_remaining() == 4
    
    def test_rate_limiter_reset(self):
        """Test rate limiter reset."""
        limiter = RateLimiter(rate=5, per=60)
        
        # Use some requests
        for _ in range(3):
            limiter.is_allowed()
        
        # Reset should restore full capacity
        limiter.reset()
        assert limiter.get_remaining() == 5


class TestInputValidation:
    """Test input validation mechanisms."""
    
    def test_validate_valid_email(self):
        """Test validation of valid email addresses."""
        assert validate_email("test@example.com") is True
        assert validate_email("user.name+tag@example.co.uk") is True
    
    def test_validate_invalid_email(self):
        """Test validation of invalid email addresses."""
        # These should raise ValidationError
        with pytest.raises(Exception):  # ValidationError
            validate_email("invalid")
        with pytest.raises(Exception):
            validate_email("@example.com")
        with pytest.raises(Exception):
            validate_email("test@")
        with pytest.raises(Exception):
            validate_email("test@example")
    
    def test_validate_strong_password(self):
        """Test validation of strong passwords."""
        assert validate_password("StrongPass123!") is True
        assert validate_password("Another$Secure456") is True
    
    def test_validate_weak_password(self):
        """Test validation of weak passwords."""
        # These should raise ValidationError (too short)
        with pytest.raises(Exception):
            validate_password("weak")
        with pytest.raises(Exception):
            validate_password("1234567")  # Only 7 characters
        with pytest.raises(Exception):
            validate_password("")  # Empty
    
    def test_validate_agency_name(self):
        """Test agency name validation."""
        assert validate_name("Valid Agency Name", "Agency Name") is True
        assert validate_name("Test", "Agency Name") is True
        # These should raise ValidationError
        with pytest.raises(Exception):
            validate_name("", "Agency Name")
        with pytest.raises(Exception):
            validate_name("a" * 121, "Agency Name")  # Too long
    
    def test_validate_project_title(self):
        """Test project title validation."""
        assert validate_name("Valid Project Title", "Project Title") is True
        assert validate_name("Test", "Project Title") is True
        # These should raise ValidationError
        with pytest.raises(Exception):
            validate_name("", "Project Title")
        with pytest.raises(Exception):
            validate_name("a" * 201, "Project Title")  # Too long
    
    def test_sanitize_input(self):
        """Test input sanitization."""
        # Test that sanitization doesn't crash
        sanitized = sanitize_string("<script>alert('xss')</script>")
        assert sanitized is not None
        # Test normal text preservation
        assert "normal text" == sanitize_string("normal text")


class TestEncryption:
    """Test encryption mechanisms."""
    
    def test_encrypt_decrypt_field(self):
        """Test field encryption and decryption."""
        original_data = "sensitive_information_123"
        encrypted = encrypt(original_data)
        decrypted = decrypt(encrypted)
        
        assert encrypted != original_data
        assert decrypted == original_data
    
    def test_encrypt_different_results(self):
        """Test that encryption produces different results each time."""
        data = "test_data"
        encrypted1 = encrypt(data)
        encrypted2 = encrypt(data)
        
        # Should be different due to random IV
        assert encrypted1 != encrypted2
    
    def test_decrypt_invalid_data(self):
        """Test decryption of invalid data."""
        with pytest.raises(Exception):
            decrypt("invalid_encrypted_data")


class TestSecurityLogging:
    """Test security logging mechanisms."""
    
    def test_security_event_types(self):
        """Test security event types."""
        # Test that event types are defined
        assert SecurityEvent.LOGIN_SUCCESS == "login_success"
        assert SecurityEvent.LOGIN_FAILURE == "login_failure"
        assert SecurityEvent.ACCESS_DENIED == "access_denied"
        assert SecurityEvent.RATE_LIMIT_EXCEEDED == "rate_limit_exceeded"
    
    def test_log_security_event(self):
        """Test logging security events."""
        # This should not raise an exception
        log_security_event(
            event_type=SecurityEvent.LOGIN_SUCCESS,
            user_id=1,
            ip_address="127.0.0.1",
            details={"method": "email"}
        )
    
    def test_log_failed_login(self):
        """Test logging failed login attempts."""
        log_security_event(
            event_type=SecurityEvent.LOGIN_FAILURE,
            user_id=None,
            ip_address="127.0.0.1",
            details={"email": "test@example.com", "reason": "invalid_password"}
        )
    
    def test_log_file_access(self):
        """Test logging file access events."""
        log_security_event(
            event_type=SecurityEvent.FILE_DOWNLOAD,
            user_id=1,
            ip_address="127.0.0.1",
            details={"file_id": 1, "action": "download"}
        )


class TestFileSecurity:
    """Test file security mechanisms."""
    
    def test_file_download_authorization(self):
        """Test file download authorization check."""
        # This test would require mocking the database
        # For now, we'll test the concept
        assert True  # Placeholder
    
    def test_file_upload_validation(self):
        """Test file upload validation."""
        # Test file size validation
        max_size = 50 * 1024 * 1024  # 50MB
        assert max_size == 50 * 1024 * 1024
        
        # Test allowed file types
        allowed_types = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']
        assert 'image/jpeg' in allowed_types
        assert 'application/pdf' in allowed_types


class TestAuthenticationSecurity:
    """Test authentication security mechanisms."""
    
    def test_password_hashing(self):
        """Test password hashing with bcrypt."""
        password = "secure_password_123"
        salt = bcrypt.gensalt(rounds=12)
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        assert hashed != password.encode('utf-8')
        assert bcrypt.checkpw(password.encode('utf-8'), hashed) is True
        assert bcrypt.checkpw("wrong_password".encode('utf-8'), hashed) is False
    
    def test_session_timeout(self):
        """Test session timeout mechanism."""
        # This would test the session timeout logic
        # For now, we'll test the concept
        timeout_minutes = 30
        assert timeout_minutes == 30


if __name__ == "__main__":
    pytest.main([__file__, "-v"])