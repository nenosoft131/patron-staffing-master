import logging
from logging.handlers import RotatingFileHandler
import os
from core.config import get_settings

settings = get_settings()

# Ensure log directory exists
os.makedirs(settings.LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(settings.LOG_DIR, "app.log")
LOG_LEVEL = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

def setup_logger(name: str = "app_logger") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    # Prevent duplicate handlers if logger is imported multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(filename)s:%(lineno)d | "
            "%(funcName)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)

    # Console handler (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False  # avoid double logging

    return logger


# Usage
logger = setup_logger()
