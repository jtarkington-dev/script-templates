#!/usr/bin/env python3
"""
retry_decorator.py
Author: Jeremy Tarkington

Reusable decorator to retry a function if it fails.
Supports:
- Retry limit
- Delay between retries
- Optional exception types to catch
"""

import time
import functools
import logging


def retry(
    max_attempts=3,
    delay=2,
    exceptions=(Exception,),
    backoff=False,
    logger=None
):
    """
    Decorator that retries a function on failure.

    Args:
        max_attempts (int): Total number of attempts (default 3)
        delay (int): Delay between attempts in seconds (default 2)
        exceptions (tuple): Exception types to catch (default Exception)
        backoff (bool): If True, doubles delay each retry
        logger (Logger): Optional logger (else prints)

    Example:
        @retry(max_attempts=5, delay=1)
        def fragile_function():
            ...
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tries = 0
            current_delay = delay
            while tries < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    tries += 1
                    msg = f"[Retry {tries}/{max_attempts}] {func.__name__} failed: {e}"
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    if tries < max_attempts:
                        time.sleep(current_delay)
                        if backoff:
                            current_delay *= 2
            raise RuntimeError(f"{func.__name__} failed after {max_attempts} attempts.")
        return wrapper
    return decorator


# === Example Usage ===
if __name__ == "__main__":
    log = logging.getLogger("retry_example")
    logging.basicConfig(level=logging.INFO)

    import random

    @retry(max_attempts=4, delay=1, backoff=True, logger=log)
    def unstable():
        if random.random() < 0.75:
            raise ValueError("Random failure occurred!")
        return "Success!"

    print(unstable())
