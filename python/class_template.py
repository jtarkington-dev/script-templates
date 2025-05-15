#!/usr/bin/env python3
"""
class_template.py
Author: Jeremy Tarkington

Reusable class structure with:
- Configurable init
- Action method
- Optional string representation
- Ready for CLI, agent, or tool integration
"""

import logging


class ExampleTool:
    def __init__(self, name="MyTool", dry_run=True, config=None):
        """
        Initialize the class with settings or config.

        Args:
            name (str): Tool name
            dry_run (bool): Enable safe 'test mode'
            config (dict): Optional custom settings
        """
        self.name = name
        self.dry_run = dry_run
        self.config = config or {}
        logging.info(f"Initialized {self.name} (dry_run={self.dry_run})")

    def do_task(self, data):
        """
        Main task logic. Accepts data or a target input.

        Args:
            data (Any): Data or payload to process
        """
        if self.dry_run:
            logging.info(f"[DRY RUN] Would process: {data}")
        else:
            logging.info(f"Processing data: {data}")
            # TODO: Add real processing logic here

    def __repr__(self):
        return f"<{self.__class__.__name__} name={self.name} dry_run={self.dry_run}>"


# ========== Example usage ==========
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    tool = ExampleTool(name="MyAgent", dry_run=False)
    tool.do_task("Sample payload")
    print(tool)
