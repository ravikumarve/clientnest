import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    """Setup application logging."""

    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = RotatingFileHandler(
        "logs/clientnest.log",
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
    )
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Health check endpoint for monitoring
def health_check():
    """Simple health check function."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "services": ["database", "auth", "files"],
    }
