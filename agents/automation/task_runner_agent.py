#!/usr/bin/env python3
"""
TaskRunnerAgent Template
Author: Jeremy Tarkington
Description:
    A reusable Python agent template that loads and runs tasks from a queue.
    Tasks can come from a list, file, or any data source.

Usage:
    python task_runner_agent.py --loop --verbose
"""

import time
import logging
import argparse
import uuid


class TaskRunnerAgent:
    def __init__(self, name: str = "TaskRunnerAgent"):
        self.name = name
        self.agent_id = str(uuid.uuid4())
        self.running = True
        self.task_queue = []
        logging.info(f"[{self.name}] Initialized with ID: {self.agent_id}")

    def load_tasks(self):
        """
        Placeholder for loading tasks into the queue.
        Replace this with loading from a file, DB, API, etc.
        """
        logging.debug("Loading tasks...")
        self.task_queue = [
            {"type": "print", "message": "Hello World"},
            {"type": "sleep", "seconds": 2},
            {"type": "print", "message": "Task completed."}
        ]

    def execute_task(self, task):
        """Handle and execute an individual task"""
        task_type = task.get("type")

        if task_type == "print":
            logging.info(f"PRINT: {task.get('message')}")
        elif task_type == "sleep":
            seconds = task.get("seconds", 1)
            logging.info(f"SLEEP: {seconds}s")
            time.sleep(seconds)
        else:
            logging.warning(f"Unknown task type: {task_type}")

    def run_once(self):
        """Load and run all tasks in the queue once"""
        logging.info("Running task batch once...")
        self.load_tasks()
        for task in self.task_queue:
            self.execute_task(task)
        logging.info("All tasks completed.")

    def run_loop(self, interval=10):
        """Run tasks in a loop with delay"""
        logging.info(f"Starting loop mode with interval {interval}s...")
        try:
            while self.running:
                self.run_once()
                logging.debug(f"Waiting {interval}s before next cycle...")
                time.sleep(interval)
        except KeyboardInterrupt:
            self.running = False
            logging.info("Loop stopped by user.")


def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def parse_args():
    parser = argparse.ArgumentParser(description="TaskRunnerAgent CLI")
    parser.add_argument("--name", type=str, default="TaskRunnerAgent", help="Name of the agent")
    parser.add_argument("--loop", action="store_true", help="Run agent in loop mode")
    parser.add_argument("--interval", type=int, default=10, help="Loop interval in seconds")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging(args.verbose)

    agent = TaskRunnerAgent(name=args.name)

    if args.loop:
        agent.run_loop(interval=args.interval)
    else:
        agent.run_once()


if __name__ == "__main__":
    main()
