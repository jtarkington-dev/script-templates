#!/usr/bin/env python3
"""
schedule_task.py
Author: Jeremy Tarkington

A reusable scheduled task runner with:
- Flexible interval scheduling
- Graceful shutdown
- Logging and separation of tasks
"""

import schedule
import time
import logging
import random


# ========== Logging ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# ========== Your Task Logic ==========
def job():
    task_id = random.randint(1000, 9999)
    logging.info(f"Running scheduled task [ID: {task_id}]...")
    # TODO: Add real task logic here
    time.sleep(1)
    logging.info(f"Task [ID: {task_id}] complete.")


# ========== Setup Schedule ==========
def schedule_tasks():
    # Runs every 10 seconds
    schedule.every(10).seconds.do(job)

    # Uncomment examples below if needed:
    # schedule.every().hour.do(job)
    # schedule.every().day.at("03:00").do(job)


# ========== Main Loop ==========
def main():
    logging.info("Starting scheduler...")
    schedule_tasks()

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user.")


# ========== Entrypoint ==========
if __name__ == "__main__":
    main()
