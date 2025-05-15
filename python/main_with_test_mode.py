#!/usr/bin/env python3
"""
main_with_test_mode.py
Author: Jeremy Tarkington

A reusable script template that supports:
- --test vs --live mode
- Clear logic branching
- Logging and safety
"""

import argparse
import logging
import sys


# ========== Logging ==========
def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


# ========== Core Actions ==========
def run_test_mode():
    logging.info("Running in TEST mode — no real changes will be made.")
    # Simulate or preview actions
    print("Simulated action 1")
    print("Simulated action 2")


def run_live_mode():
    logging.warning("Running in LIVE mode — changes will be permanent!")
    # Real actions go here
    print("Performing action 1...")
    print("Performing action 2...")


# ========== Main ==========
def main(args):
    if args.test:
        run_test_mode()
    elif args.live:
        run_live_mode()
    else:
        logging.error("You must specify either --test or --live.")
        sys.exit(1)


# ========== CLI ==========
def parse_args():
    parser = argparse.ArgumentParser(description="Script with test/live mode.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--test", action="store_true", help="Run in test (dry-run) mode")
    mode.add_argument("--live", action="store_true", help="Run in live (real execution) mode")
    parser.add_argument("--verbose", action="store_true", help="Enable debug output")
    return parser.parse_args()


# ========== Entrypoint ==========
if __name__ == "__main__":
    args = parse_args()
    setup_logging(args.verbose)

    try:
        main(args)
    except KeyboardInterrupt:
        logging.warning("Script interrupted by user.")
        sys.exit(1)
    except Exception as e:
        logging.exception(f"Unhandled error: {e}")
        sys.exit(1)
