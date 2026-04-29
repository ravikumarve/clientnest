"""Rate limiting utilities for Clientnest API endpoints."""
import time
import logging
from collections import defaultdict
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class RateLimiter:
    """Token bucket rate limiter for API endpoints."""
    
    def __init__(self, rate: int, per: int = 60):
        """Initialize the rate limiter.
        
        Args:
            rate: Maximum number of requests allowed.
            per: Time period in seconds (default: 60).
        """
        self.rate = rate
        self.per = per
        self.allowance = rate
        self.last_check = time.time()
        self._storage: Dict[str, Dict] = defaultdict(lambda: {
            "allowance": rate,
            "last_check": time.time()
        })
    
    def _get_key(self) -> str:
        """Get a unique key for the current session/user.
        
        Returns:
            A unique identifier for rate limiting.
        """
        # For now, use a simple key based on the object id
        # In production, this would use session/user ID from Reflex state
        return f"anonymous:{id(self)}"
    
    def is_allowed(self) -> bool:
        """Check if the current request is allowed under the rate limit.
        
        Returns:
            True if the request is allowed, False otherwise.
        """
        key = self._get_key()
        current = time.time()
        time_passed = current - self._storage[key]["last_check"]
        
        # Refill the bucket based on time passed
        self._storage[key]["last_check"] = current
        self._storage[key]["allowance"] += time_passed * (self.rate / self.per)
        
        # Cap the allowance at the maximum rate
        if self._storage[key]["allowance"] > self.rate:
            self._storage[key]["allowance"] = self.rate
        
        # Check if we have enough allowance
        if self._storage[key]["allowance"] < 1.0:
            return False
        
        # Consume one token
        self._storage[key]["allowance"] -= 1.0
        return True
    
    def get_remaining(self) -> int:
        """Get the number of remaining requests in the current time window.
        
        Returns:
            The number of remaining requests.
        """
        key = self._get_key()
        return int(self._storage[key]["allowance"])
    
    def get_reset_time(self) -> float:
        """Get the time when the rate limit will reset.
        
        Returns:
            Unix timestamp when the rate limit will reset.
        """
        key = self._get_key()
        # Calculate when the bucket will be full again
        deficit = self.rate - self._storage[key]["allowance"]
        if deficit <= 0:
            return time.time()
        time_to_fill = deficit / (self.rate / self.per)
        return time.time() + time_to_fill
    
    def reset(self) -> None:
        """Reset the rate limit for the current session/user."""
        key = self._get_key()
        self._storage[key] = {
            "allowance": self.rate,
            "last_check": time.time()
        }


# Pre-configured rate limiters for different endpoints
LOGIN_RATE_LIMITER = RateLimiter(rate=5, per=300)  # 5 login attempts per 5 minutes
API_RATE_LIMITER = RateLimiter(rate=100, per=60)   # 100 API requests per minute
WEBHOOK_RATE_LIMITER = RateLimiter(rate=10, per=60)  # 10 webhook requests per minute
UPLOAD_RATE_LIMITER = RateLimiter(rate=20, per=60)  # 20 file uploads per minute


def check_rate_limit(limiter: RateLimiter) -> tuple[bool, int, float]:
    """Check if a request is allowed under the rate limit.
    
    Args:
        limiter: The rate limiter to check.
        
    Returns:
        A tuple of (is_allowed, remaining_requests, reset_time).
    """
    is_allowed = limiter.is_allowed()
    remaining = limiter.get_remaining()
    reset_time = limiter.get_reset_time()
    
    return is_allowed, remaining, reset_time


def get_rate_limit_headers(limiter: RateLimiter) -> Dict[str, str]:
    """Get rate limit headers for the response.
    
    Args:
        limiter: The rate limiter to get headers for.
        
    Returns:
        A dictionary of rate limit headers.
    """
    remaining = limiter.get_remaining()
    reset_time = limiter.get_reset_time()
    
    return {
        "X-RateLimit-Limit": str(limiter.rate),
        "X-RateLimit-Remaining": str(remaining),
        "X-RateLimit-Reset": str(int(reset_time)),
    }
