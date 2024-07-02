import logging
import logging.config
from app.config import settings

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'RESET': '\033[0m',
        'BOLD': '\033[1m',
        'RED': '\033[31m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'CYAN': '\033[36m',
    }

    def format(self, record):
        log_level_color = {
            logging.DEBUG: ColoredFormatter.COLORS['BLUE'],
            logging.INFO: ColoredFormatter.COLORS['GREEN'],
            logging.WARNING: ColoredFormatter.COLORS['YELLOW'],
            logging.ERROR: ColoredFormatter.COLORS['RED'],
            logging.CRITICAL: ColoredFormatter.COLORS['BOLD'] + ColoredFormatter.COLORS['RED'],
        }.get(record.levelno, ColoredFormatter.COLORS['RESET'])

        message = super().format(record)
        return f"{log_level_color}{message}{ColoredFormatter.COLORS['RESET']}"


# Load the logging configuration
logging.config.fileConfig('logging.ini')

# Get the root logger
logger = logging.getLogger()
logger.setLevel(settings.LOG_LEVEL)

# Update other loggers
logging.getLogger('fastapi').setLevel(settings.LOG_LEVEL)
logging.getLogger("uvicorn").setLevel(settings.LOG_LEVEL)

# Apply the custom color formatter to the console handler
for handler in logger.handlers:
    if isinstance(handler, logging.StreamHandler):
        handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s'))