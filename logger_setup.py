"""
logger_setup.py

Centralized loguru-based logger configuration for all scripts.
Includes:
- File logging with rotation and full tracebacks
- Pretty colored console logging
- Global exception hook
"""

import sys
from loguru import logger


# --- File Logger Setup ---
logger.remove()  # remove default sink (stdout)
logger.add(
    "labels_sync.log",
    level="DEBUG",
    rotation="1 MB",
    backtrace=True,
    diagnose=True
)


def _handle_exception(exc_type, exc_value, exc_traceback):
    """
    Handles uncaught exceptions globally and logs them using loguru.
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.opt(exception=(exc_type, exc_value, exc_traceback)).error("Uncaught exception")


sys.excepthook = _handle_exception


def configure_console_logger(level: str = "INFO"):
    """
    Adds a colorized console output sink to loguru.

    Args:
        level (str): Logging level (DEBUG, INFO, WARNING, ERROR)
    """
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{level:<8}</level> | {message}",
        level=level.upper(),
        colorize=True
    )
