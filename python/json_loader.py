#!/usr/bin/env python3
"""
json_loader.py
Author: Jeremy Tarkington

Reusable JSON file loader with:
- File existence check
- JSON decode error handling
- Optional default fallback
"""

import json
import os
import logging


def load_json(filepath, default=None, logger=None):
    """
    Safely load a JSON file with fallback if not found or invalid.

    Args:
        filepath (str): Path to the JSON file.
        default (Any): Value to return if file is missing or fails to load.
        logger (Logger): Optional logger to log errors.

    Returns:
        dict or fallback value.
    """
    if not os.path.exists(filepath):
        msg = f"JSON file not found: {filepath}"
        if logger:
            logger.warning(msg)
        else:
            print(f"[WARN] {msg}")
        return default

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        msg = f"Invalid JSON in {filepath}: {e}"
        if logger:
            logger.error(msg)
        else:
            print(f"[ERROR] {msg}")
        return default


def save_json(filepath, data, indent=2):
    """
    Save a dictionary to a JSON file.

    Args:
        filepath (str): Output path.
        data (dict): JSON-serializable content.
        indent (int): Pretty-print spacing.
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)
    print(f"Saved JSON to: {filepath}")


# === Example ===
if __name__ == "__main__":
    test_file = "config.json"
    fallback = {"debug": True, "timeout": 10}

    config = load_json(test_file, default=fallback)
    print(config)

    # Save it back for testing
    save_json("config_saved.json", config)
