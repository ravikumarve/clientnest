"""Security middleware for Clientnest."""
import time
from typing import Callable

from reflex import Middleware
from reflex.utils.logging import log

from .error_handler import RateLimitError
from .rate_limiter import (
    API_RATE_LIMITER,
    LOGIN_RATE_LIMITER,
    UPLOAD_RATE_LIMITER,
    WEBHOOK_RATE_LIMITER,
    check_rate_limit,
    get_rate_limit_headers,
)
from .security_logger import log_security_event, SecurityEvent


class SecurityHeadersMiddleware(Middleware):
    """Middleware to add security headers to all responses."""
    
    async def __call__(self, app: Callable) -> Callable:
        """Apply security headers middleware.
        
        Args:
            app: The next middleware or app in the chain.
            
        Returns:
            The wrapped app.
        """
        async def wrapper(scope, receive, send):
            """Wrapper function to add security headers."""
            
            async def send_wrapper(message):
                """Wrapper to modify response headers."""
                if message["type"] == "http.response.start":
                    headers = dict(message.get("headers", []))
                    
                    # Add security headers
                    headers[b"X-Content-Type-Options"] = b"nosniff"
                    headers[b"X-Frame-Options"] = b"DENY"
                    headers[b"X-XSS-Protection"] = b"1; mode=block"
                    headers[b"Strict-Transport-Security"] = b"max-age=31536000; includeSubDomains"
                    headers[b"Content-Security-Policy"] = b"default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self'; frame-ancestors 'none';"
                    headers[b"Referrer-Policy"] = b"strict-origin-when-cross-origin"
                    headers[b"Permissions-Policy"] = b"geolocation=(), microphone=(), camera=()"
                    
                    message["headers"] = list(headers.items())
                
                await send(message)
            
            await app(scope, receive, send_wrapper)
        
        return wrapper


class RateLimitMiddleware(Middleware):
    """Middleware to apply rate limiting to API endpoints."""
    
    def __init__(self, limiter, endpoint_name: str = "api"):
        """Initialize the rate limit middleware.
        
        Args:
            limiter: The rate limiter to use.
            endpoint_name: The name of the endpoint for logging.
        """
        self.limiter = limiter
        self.endpoint_name = endpoint_name
    
    async def __call__(self, app: Callable) -> Callable:
        """Apply rate limiting middleware.
        
        Args:
            app: The next middleware or app in the chain.
            
        Returns:
            The wrapped app.
        """
        async def wrapper(scope, receive, send):
            """Wrapper to apply rate limiting."""
            # Check rate limit
            is_allowed, remaining, reset_time = check_rate_limit(self.limiter)
            
            if not is_allowed:
                # Rate limit exceeded
                log_security_event(
                    event_type=SecurityEvent.RATE_LIMIT_EXCEEDED,
                    details={
                        "endpoint": self.endpoint_name,
                        "reset_time": reset_time,
                    }
                )
                
                # Send rate limit error response
                await send({
                    "type": "http.response.start",
                    "status": 429,
                    "headers": [
                        [b"content-type", b"application/json"],
                        *get_rate_limit_headers(self.limiter).items(),
                    ],
                })
                await send({
                    "type": "http.response.body",
                    "body": b'{"error": "RateLimitError", "message": "Too many requests. Please try again later."}',
                })
                return
            
            # Add rate limit headers to response
            async def send_wrapper(message):
                """Wrapper to add rate limit headers."""
                if message["type"] == "http.response.start":
                    headers = dict(message.get("headers", []))
                    headers.update(get_rate_limit_headers(self.limiter))
                    message["headers"] = list(headers.items())
                
                await send(message)
            
            await app(scope, receive, send_wrapper)
        
        return wrapper


class RequestLoggingMiddleware(Middleware):
    """Middleware to log all requests for security monitoring."""
    
    async def __call__(self, app: Callable) -> Callable:
        """Apply request logging middleware.
        
        Args:
            app: The next middleware or app in the chain.
            
        Returns:
            The wrapped app.
        """
        async def wrapper(scope, receive, send):
            """Wrapper to log requests."""
            start_time = time.time()
            
            # Extract request information
            method = scope.get("method", "UNKNOWN")
            path = scope.get("path", "/")
            client_host = scope.get("client", ("", ""))[0]
            user_agent = scope.get("headers", {}).get(b"user-agent", b"").decode()
            
            # Log request
            log(f"Request: {method} {path} from {client_host}", level="info")
            
            # Process request
            await app(scope, receive, send)
            
            # Log response time
            duration = time.time() - start_time
            log(f"Response: {method} {path} completed in {duration:.3f}s", level="info")
        
        return wrapper


class CORSMiddleware(Middleware):
    """Middleware to handle CORS for API endpoints."""
    
    def __init__(
        self,
        allow_origins: list[str] = None,
        allow_methods: list[str] = None,
        allow_headers: list[str] = None,
        allow_credentials: bool = False,
    ):
        """Initialize the CORS middleware.
        
        Args:
            allow_origins: List of allowed origins.
            allow_methods: List of allowed methods.
            allow_headers: List of allowed headers.
            allow_credentials: Whether to allow credentials.
        """
        self.allow_origins = allow_origins or ["*"]
        self.allow_methods = allow_methods or ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
        self.allow_headers = allow_headers or ["Content-Type", "Authorization"]
        self.allow_credentials = allow_credentials
    
    async def __call__(self, app: Callable) -> Callable:
        """Apply CORS middleware.
        
        Args:
            app: The next middleware or app in the chain.
            
        Returns:
            The wrapped app.
        """
        async def wrapper(scope, receive, send):
            """Wrapper to handle CORS."""
            # Handle preflight requests
            if scope["method"] == "OPTIONS":
                await send({
                    "type": "http.response.start",
                    "status": 200,
                    "headers": self._get_cors_headers(),
                })
                await send({
                    "type": "http.response.body",
                    "body": b"",
                })
                return
            
            # Add CORS headers to response
            async def send_wrapper(message):
                """Wrapper to add CORS headers."""
                if message["type"] == "http.response.start":
                    headers = dict(message.get("headers", []))
                    headers.update(self._get_cors_headers())
                    message["headers"] = list(headers.items())
                
                await send(message)
            
            await app(scope, receive, send_wrapper)
        
        return wrapper
    
    def _get_cors_headers(self) -> list[tuple[bytes, bytes]]:
        """Get CORS headers.
        
        Returns:
            A list of CORS headers.
        """
        headers = [
            (b"Access-Control-Allow-Origin", ", ".join(self.allow_origins).encode()),
            (b"Access-Control-Allow-Methods", ", ".join(self.allow_methods).encode()),
            (b"Access-Control-Allow-Headers", ", ".join(self.allow_headers).encode()),
        ]
        
        if self.allow_credentials:
            headers.append((b"Access-Control-Allow-Credentials", b"true"))
        
        return headers


# Pre-configured middleware instances
security_headers_middleware = SecurityHeadersMiddleware()
request_logging_middleware = RequestLoggingMiddleware()

login_rate_limit_middleware = RateLimitMiddleware(LOGIN_RATE_LIMITER, "login")
api_rate_limit_middleware = RateLimitMiddleware(API_RATE_LIMITER, "api")
webhook_rate_limit_middleware = RateLimitMiddleware(WEBHOOK_RATE_LIMITER, "webhook")
upload_rate_limit_middleware = RateLimitMiddleware(UPLOAD_RATE_LIMITER, "upload")

cors_middleware = CORSMiddleware(
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-CSRF-Token"],
    allow_credentials=True,
)
