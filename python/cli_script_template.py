#!/usr/bin/env python3
"""
cli_script_template.py
Author: Jeremy Tarkington

A reusable CLI Python script template with:
- Argparse argument handling
- Logging setup with verbosity toggle
- Structured main() logic
"""

import argparse
import logging
import sys


# ========== Logging Setup ==========
def setup_logging(verbose: bool):
    """Configure logging format and level"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


# ========== Main Logic ==========
def main(args):
    logging.info("Script started.")
    
    # === Placeholder task ===
    logging.debug(f"Received input: {args.input}")
    print(f"Hello, {args.input}!")

    logging.info("Script completed successfully.")


# ========== Argument Parsing ==========
def parse_args():
    parser = argparse.ArgumentParser(
        description="Starter CLI script with argparse and logging."
    )
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Input string to process"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging"
    )
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
