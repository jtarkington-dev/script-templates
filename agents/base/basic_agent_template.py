#!/usr/bin/env python3
"""
BasicAgent Template
Author: Jeremy Tarkington
Description:
    A reusable agent scaffold in Python that can be extended for AI, automation, monitoring, etc.

Usage:
    python basic_agent_template.py --name "MyAgent" --loop
"""

import time
import argparse
import logging
import uuid


class BasicAgent:
    def __init__(self, name: str):
        self.name = name
        self.agent_id = str(uuid.uuid4())  # Unique ID for tracking/logging
        self.running = True
        logging.info(f"Agent '{self.name}' initialized with ID: {self.agent_id}")

    def run_once(self):
        """Runs a single task cycle"""
        logging.info(f"[{self.name}] Running single task cycle...")
        # TODO: Add actual task logic here
        print(f"{self.name} is doing a task...")
        time.sleep(1)

    def run_loop(self):
        """Runs the agent continuously until stopped"""
        logging.info(f"[{self.name}] Starting loop. Press Ctrl+C to stop.")
        try:
            while self.running:
                self.run_once()
        except KeyboardInterrupt:
            self.running = False
            logging.info(f"[{self.name}] Received keyboard interrupt. Shutting down...")


def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def parse_args():
    parser = argparse.ArgumentParser(description="Run a basic agent")
    parser.add_argument("--name", type=str, default="BasicAgent", help="Name of the agent")
    parser.add_argument("--loop", action="store_true", help="Run the agent in a continuous loop")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging(args.verbose)

    agent = BasicAgent(name=args.name)

    if args.loop:
        agent.run_loop()
    else:
        agent.run_once()


if __name__ == "__main__":
    main()
