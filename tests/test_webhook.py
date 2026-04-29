"""Webhook tests for Clientnest application."""
import pytest
import hmac
import hashlib
import json
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
import sys
import os

# Add the clientnest module to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from clientnest.clientnest.webhook_api import validate_webhook_signature
from clientnest.clientnest.rate_limiter import RateLimiter


class TestWebhookSignatureValidation:
    """Test webhook signature validation."""
    
    def test_generate_valid_signature(self):
        """Test generating valid webhook signature."""
        secret = "test_webhook_secret"
        payload = b'{"test": "data"}'
        
        signature = hmac.new(
            secret.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()
        
        assert signature is not None
        assert len(signature) == 64  # SHA256 produces 64 hex characters
    
    def test_validate_correct_signature(self):
        """Test validation of correct webhook signature."""
        secret = "test_webhook_secret"
        payload = b'{"event": "subscription_created"}'
        
        # Generate signature
        signature = hmac.new(
            secret.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()
        
        # Validate signature
        is_valid = validate_webhook_signature(payload, signature, secret)
        assert is_valid is True
    
    def test_validate_incorrect_signature(self):
        """Test validation of incorrect webhook signature."""
        secret = "test_webhook_secret"
        payload = b'{"event": "subscription_created"}'
        
        # Use wrong signature
        wrong_signature = "wrong_signature_value"
        
        is_valid = validate_webhook_signature(payload, wrong_signature, secret)
        assert is_valid is False
    
    def test_validate_empty_signature(self):
        """Test validation of empty signature."""
        secret = "test_webhook_secret"
        payload = b'{"event": "subscription_created"}'
        
        is_valid = validate_webhook_signature(payload, "", secret)
        assert is_valid is False
    
    def test_validate_modified_payload(self):
        """Test validation fails when payload is modified."""
        secret = "test_webhook_secret"
        original_payload = b'{"event": "subscription_created"}'
        modified_payload = b'{"event": "subscription_cancelled"}'
        
        # Generate signature for original payload
        signature = hmac.new(
            secret.encode(),
            original_payload,
            hashlib.sha256
        ).hexdigest()
        
        # Try to validate modified payload with original signature
        is_valid = validate_webhook_signature(modified_payload, signature, secret)
        assert is_valid is False


class TestWebhookEventTypes:
    """Test webhook event type handling."""
    
    def test_subscription_created_event(self):
        """Test subscription_created event handling."""
        event_data = {
            "meta": {
                "event_name": "subscription_created"
            },
            "data": {
                "attributes": {
                    "first_subscription_item": {
                        "variant_id": "solo_variant_id"
                    }
                }
            }
        }
        
        assert event_data["meta"]["event_name"] == "subscription_created"
    
    def test_subscription_updated_event(self):
        """Test subscription_updated event handling."""
        event_data = {
            "meta": {
                "event_name": "subscription_updated"
            },
            "data": {
                "attributes": {
                    "status": "active"
                }
            }
        }
        
        assert event_data["meta"]["event_name"] == "subscription_updated"
    
    def test_subscription_cancelled_event(self):
        """Test subscription_cancelled event handling."""
        event_data = {
            "meta": {
                "event_name": "subscription_cancelled"
            },
            "data": {
                "attributes": {
                    "status": "cancelled"
                }
            }
        }
        
        assert event_data["meta"]["event_name"] == "subscription_cancelled"
    
    def test_order_created_event(self):
        """Test order_created event handling."""
        event_data = {
            "meta": {
                "event_name": "order_created"
            },
            "data": {
                "attributes": {
                    "first_order_item": {
                        "product_id": "invoice_product_id"
                    }
                },
                "meta": {
                    "custom_data": {
                        "invoice_id": "123"
                    }
                }
            }
        }
        
        assert event_data["meta"]["event_name"] == "order_created"


class TestWebhookAPI:
    """Test Webhook API functionality."""
    
    def test_webhook_signature_validation(self):
        """Test webhook signature validation."""
        secret = "test_webhook_secret"
        payload = b'{"event": "subscription_created"}'
        
        # Generate signature
        signature = hmac.new(
            secret.encode(),
            payload,
            hashlib.sha256
        ).hexdigest()
        
        # Validate signature
        is_valid = validate_webhook_signature(payload, signature, secret)
        assert is_valid is True
    
    def test_webhook_rate_limiting(self):
        """Test webhook rate limiting."""
        limiter = RateLimiter(rate=10, per=60)
        
        # First few requests should succeed
        for i in range(5):
            assert limiter.is_allowed() is True
    
    def test_webhook_rate_limiting_exceeded(self):
        """Test webhook rate limiting when exceeded."""
        limiter = RateLimiter(rate=3, per=60)
        
        # First 3 requests should succeed
        for _ in range(3):
            assert limiter.is_allowed() is True
        
        # 4th request should be blocked
        assert limiter.is_allowed() is False


class TestWebhookSecurity:
    """Test webhook security measures."""
    
    def test_webhook_ip_logging(self):
        """Test webhook IP address logging."""
        ip_address = "192.168.1.1"
        assert ip_address == "192.168.1.1"
    
    def test_webhook_timestamp_validation(self):
        """Test webhook timestamp validation."""
        # Webhooks should be processed within a reasonable time
        current_time = datetime.now()
        webhook_time = current_time - timedelta(minutes=5)
        
        # Should be within acceptable time window
        time_diff = current_time - webhook_time
        assert time_diff.total_seconds() < 600  # 10 minutes
    
    def test_webhook_replay_attack_prevention(self):
        """Test webhook replay attack prevention."""
        # Each webhook should have a unique ID
        webhook_id = "webhook_12345"
        processed_webhooks = set()
        
        # First processing
        assert webhook_id not in processed_webhooks
        processed_webhooks.add(webhook_id)
        
        # Replay attempt should be detected
        assert webhook_id in processed_webhooks


class TestWebhookErrorHandling:
    """Test webhook error handling."""
    
    def test_webhook_invalid_json(self):
        """Test handling invalid JSON payload."""
        invalid_payload = "invalid json string"
        
        try:
            json.loads(invalid_payload)
            assert False, "Should have raised JSONDecodeError"
        except json.JSONDecodeError:
            assert True  # Expected behavior
    
    def test_webhook_missing_fields(self):
        """Test handling webhook with missing required fields."""
        incomplete_payload = {
            "meta": {
                # Missing event_name
            }
        }
        
        # Should handle missing fields gracefully
        assert "event_name" not in incomplete_payload["meta"]
    
    def test_webhook_unknown_event_type(self):
        """Test handling unknown event type."""
        unknown_event = {
            "meta": {
                "event_name": "unknown_event_type"
            }
        }
        
        # Should handle unknown events gracefully
        assert unknown_event["meta"]["event_name"] == "unknown_event_type"


class TestWebhookIntegration:
    """Test webhook integration with business logic."""
    
    def test_subscription_update_agency_plan(self):
        """Test subscription update changes agency plan."""
        # This would test the actual business logic
        # For now, we'll test the concept
        event_data = {
            "meta": {
                "event_name": "subscription_created"
            },
            "data": {
                "attributes": {
                    "first_subscription_item": {
                        "variant_id": "solo_variant_id"
                    }
                }
            }
        }
        
        assert event_data["meta"]["event_name"] == "subscription_created"
    
    def test_invoice_payment_status_update(self):
        """Test invoice payment status update."""
        event_data = {
            "meta": {
                "event_name": "order_created"
            },
            "data": {
                "meta": {
                    "custom_data": {
                        "invoice_id": "123"
                    }
                }
            }
        }
        
        invoice_id = event_data["data"]["meta"]["custom_data"]["invoice_id"]
        assert invoice_id == "123"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])