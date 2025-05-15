#!/usr/bin/env python3
"""
SystemMonitorAgent Template
Author: Jeremy Tarkington
Description:
    A loop-based agent that monitors CPU, memory, and disk usage.
    Extendable for alerts, logs, or remote reporting.

Usage:
    python system_monitor_agent.py --interval 15 --loop --verbose
"""

import time
import logging
import argparse
import uuid
import psutil  # pip install psutil


class SystemMonitorAgent:
    def __init__(self, name="SystemMonitorAgent"):
        self.name = name
        self.agent_id = str(uuid.uuid4())
        self.running = True
        logging.info(f"[{self.name}] Initialized with ID: {self.agent_id}")

    def get_metrics(self):
        """Collect system metrics and return them as a dictionary"""
        metrics = {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage("/").percent
        }
        logging.debug(f"Metrics collected: {metrics}")
        return metrics

    def report_metrics(self, metrics: dict):
        """Log or send metrics to a destination (file, server, etc.)"""
        logging.info(f"CPU: {metrics['cpu_percent']}% | "
                     f"Memory: {metrics['memory_percent']}% | "
                     f"Disk: {metrics['disk_percent']}%")

    def run_once(self):
        """Run a single monitoring cycle"""
        metrics = self.get_metrics()
        self.report_metrics(metrics)

    def run_loop(self, interval=10):
        """Continuously monitor system health"""
        logging.info(f"[{self.name}] Starting loop every {interval} seconds. Press Ctrl+C to stop.")
        try:
            while self.running:
                self.run_once()
                time.sleep(interval)
        except KeyboardInterrupt:
            self.running = False
            logging.info(f"[{self.name}] Shutdown requested by user.")


def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def parse_args():
    parser = argparse.ArgumentParser(description="SystemMonitorAgent CLI")
    parser.add_argument("--name", type=str, default="SystemMonitorAgent", help="Agent name")
    parser.add_argument("--interval", type=int, default=10, help="Interval between checks (sec)")
    parser.add_argument("--loop", action="store_true", help="Run continuously")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging(args.verbose)

    agent = SystemMonitorAgent(name=args.name)

    if args.loop:
        agent.run_loop(interval=args.interval)
    else:
        agent.run_once()


if __name__ == "__main__":
    main()
