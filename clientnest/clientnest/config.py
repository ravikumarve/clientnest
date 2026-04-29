"""Configuration settings for Clientnest."""
import os
from typing import Optional


class Config:
    """Application configuration."""
    
    # App settings
    APP_NAME: str = "Clientnest"
    APP_VERSION: str = "1.0.0"
    APP_URL: str = os.environ.get("APP_URL", "http://localhost:3000")
    
    # Database settings
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///clientnest.db")
    
    # Security settings
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "your-secret-key-here")
    ENCRYPTION_KEY: Optional[str] = os.environ.get("ENCRYPTION_KEY")
    
    # Session settings
    SESSION_TIMEOUT: int = int(os.environ.get("SESSION_TIMEOUT", "3600"))  # 1 hour
    MAX_LOGIN_ATTEMPTS: int = int(os.environ.get("MAX_LOGIN_ATTEMPTS", "5"))
    LOCKOUT_DURATION: int = int(os.environ.get("LOCKOUT_DURATION", "900"))  # 15 minutes
    
    # File upload settings
    MAX_FILE_SIZE: int = int(os.environ.get("MAX_FILE_SIZE", str(50 * 1024 * 1024)))  # 50MB
    ALLOWED_FILE_TYPES: list[str] = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/webp",
        "application/pdf",
        "text/plain",
        "text/csv",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/zip",
    ]
    UPLOAD_DIR: str = os.environ.get("UPLOAD_DIR", "uploads")
    
    # Email settings
    SMTP_HOST: Optional[str] = os.environ.get("SMTP_HOST")
    SMTP_PORT: int = int(os.environ.get("SMTP_PORT", "587"))
    SMTP_USER: Optional[str] = os.environ.get("SMTP_USER")
    SMTP_PASS: Optional[str] = os.environ.get("SMTP_PASS")
    SMTP_USE_TLS: bool = os.environ.get("SMTP_USE_TLS", "true").lower() == "true"
    EMAIL_FROM: str = os.environ.get("EMAIL_FROM", "noreply@clientnest.com")
    EMAIL_FROM_NAME: str = os.environ.get("EMAIL_FROM_NAME", "Clientnest")
    
    # LemonSqueezy settings
    LEMONSQUEEZY_API_KEY: Optional[str] = os.environ.get("LEMONSQUEEZY_API_KEY")
    LEMONSQUEEZY_WEBHOOK_SECRET: Optional[str] = os.environ.get("LEMONSQUEEZY_WEBHOOK_SECRET")
    LEMONSQUEEZY_STORE_ID: Optional[str] = os.environ.get("LEMONSQUEEZY_STORE_ID")
    LEMONSQUEEZY_SOLO_VARIANT_ID: Optional[str] = os.environ.get("LEMONSQUEEZY_SOLO_VARIANT_ID")
    LEMONSQUEEZY_AGENCY_VARIANT_ID: Optional[str] = os.environ.get("LEMONSQUEEZY_AGENCY_VARIANT_ID")
    LEMONSQUEEZY_STUDIO_VARIANT_ID: Optional[str] = os.environ.get("LEMONSQUEEZY_STUDIO_VARIANT_ID")
    
    # Plan settings
    PLAN_LIMITS: dict = {
        "free": {
            "clients": 2,
            "projects": 3,
            "storage": 500 * 1024 * 1024,  # 500MB
            "team_members": 1,
            "white_label": False,
            "custom_domain": False,
            "invoicing": False,
        },
        "solo": {
            "clients": float("inf"),
            "projects": float("inf"),
            "storage": 5 * 1024 * 1024 * 1024,  # 5GB
            "team_members": 1,
            "white_label": True,
            "custom_domain": False,
            "invoicing": True,
        },
        "agency": {
            "clients": float("inf"),
            "projects": float("inf"),
            "storage": 20 * 1024 * 1024 * 1024,  # 20GB
            "team_members": 5,
            "white_label": True,
            "custom_domain": True,
            "invoicing": True,
        },
        "studio": {
            "clients": float("inf"),
            "projects": float("inf"),
            "storage": 100 * 1024 * 1024 * 1024,  # 100GB
            "team_members": float("inf"),
            "white_label": True,
            "custom_domain": True,
            "invoicing": True,
        },
    }
    
    # Rate limiting settings
    RATE_LIMITS: dict = {
        "login": {"rate": 5, "per": 300},  # 5 attempts per 5 minutes
        "api": {"rate": 100, "per": 60},  # 100 requests per minute
        "webhook": {"rate": 10, "per": 60},  # 10 requests per minute
        "upload": {"rate": 20, "per": 60},  # 20 uploads per minute
    }
    
    # Logging settings
    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")
    LOG_FILE: Optional[str] = os.environ.get("LOG_FILE")
    
    # Feature flags
    ENABLE_REGISTRATION: bool = os.environ.get("ENABLE_REGISTRATION", "true").lower() == "true"
    ENABLE_INVITES: bool = os.environ.get("ENABLE_INVITES", "true").lower() == "true"
    ENABLE_INVOICING: bool = os.environ.get("ENABLE_INVOICING", "true").lower() == "true"
    ENABLE_WHITE_LABEL: bool = os.environ.get("ENABLE_WHITE_LABEL", "true").lower() == "true"
    
    # CORS settings
    CORS_ALLOW_ORIGINS: list[str] = os.environ.get("CORS_ALLOW_ORIGINS", "*").split(",")
    CORS_ALLOW_METHODS: list[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    CORS_ALLOW_HEADERS: list[str] = ["Content-Type", "Authorization", "X-CSRF-Token"]
    CORS_ALLOW_CREDENTIALS: bool = True
    
    @classmethod
    def get_plan_limit(cls, plan: str, resource: str) -> int:
        """Get the limit for a specific resource in a plan.
        
        Args:
            plan: The plan name.
            resource: The resource name.
            
        Returns:
            The limit for the resource, or 0 if not found.
        """
        return cls.PLAN_LIMITS.get(plan, {}).get(resource, 0)
    
    @classmethod
    def has_feature(cls, plan: str, feature: str) -> bool:
        """Check if a plan has a specific feature.
        
        Args:
            plan: The plan name.
            feature: The feature name.
            
        Returns:
            True if the plan has the feature, False otherwise.
        """
        return cls.PLAN_LIMITS.get(plan, {}).get(feature, False)
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if the app is running in production.
        
        Returns:
            True if in production, False otherwise.
        """
        return os.environ.get("ENVIRONMENT", "development") == "production"
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if the app is running in development.
        
        Returns:
            True if in development, False otherwise.
        """
        return os.environ.get("ENVIRONMENT", "development") == "development"


# Global config instance
config = Config()
