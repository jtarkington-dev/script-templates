#!/usr/bin/env python3
"""
threaded_worker.py
Author: Jeremy Tarkington

Reusable threaded worker pattern:
- Spawns N threads
- Processes tasks from a queue
- Safe logging and graceful shutdown
"""

import threading
import queue
import time
import logging
import random


# ========== Logging ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s",
    datefmt="%H:%M:%S"
)


# ========== Worker Function ==========
def worker(task_queue: queue.Queue):
    while True:
        try:
            task = task_queue.get(timeout=3)  # Wait for task
        except queue.Empty:
            logging.info("No more tasks. Exiting thread.")
            break

        try:
            logging.info(f"Processing task: {task}")
            time.sleep(random.uniform(0.5, 1.5))  # Simulate work
            logging.info(f"Completed: {task}")
        except Exception as e:
            logging.exception(f"Error processing task: {e}")
        finally:
            task_queue.task_done()


# ========== Main ==========
def main():
    NUM_WORKERS = 4
    tasks = [f"Task-{i}" for i in range(10)]

    task_queue = queue.Queue()
    for task in tasks:
        task_queue.put(task)

    threads = []
    for i in range(NUM_WORKERS):
        t = threading.Thread(target=worker, args=(task_queue,), name=f"Worker-{i+1}")
        t.start()
        threads.append(t)

    task_queue.join()  # Wait for all tasks to complete
    logging.info("All tasks completed.")

    # Optional: Wait for threads to exit cleanly
    for t in threads:
        t.join()


# ========== Entrypoint ==========
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Interrupted by user.")
