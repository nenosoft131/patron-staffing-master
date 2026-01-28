import logging
from logging.handlers import RotatingFileHandler
import os
from core.config import get_settings
setting = get_settings()

os.makedirs(setting.LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(setting.LOG_DIR, "app.log")

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO) 

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5*1024*1024, backupCount=3)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)
