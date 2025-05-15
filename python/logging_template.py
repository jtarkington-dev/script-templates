#!/usr/bin/env python3
"""
logging_template.py
Author: Jeremy Tarkington

Reusable logging setup:
- Console output
- Optional file logging
- Supports verbosity
- Optional color support
"""

import logging
import sys
from logging.handlers import RotatingFileHandler


def setup_logger(name="Logger", verbose=False, log_to_file=False, filename="app.log"):
    """
    Returns a configured logger instance.
    
    Args:
        name (str): Logger name
        verbose (bool): Enables DEBUG level
        log_to_file (bool): Enables rotating file logging
        filename (str): File path for log output

    Returns:
        logging.Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # Clear previous handlers (in case of re-runs in notebooks or tests)
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_format = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)

    # Optional File Handler
    if log_to_file:
        file_handler = RotatingFileHandler(
            filename, maxBytes=1_000_000, backupCount=3
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            fmt="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger


# === Example standalone usage ===
if __name__ == "__main__":
    log = setup_logger(verbose=True, log_to_file=True)

    log.debug("This is a DEBUG message.")
    log.info("This is an INFO message.")
    log.warning("This is a WARNING.")
    log.error("This is an ERROR.")
    log.critical("This is a CRITICAL message.")
