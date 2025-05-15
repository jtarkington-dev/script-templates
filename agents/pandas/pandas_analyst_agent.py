#!/usr/bin/env python3
"""
PandasAnalystAgent Template
Author: Jeremy Tarkington
Description:
    A reusable agent that loads a dataset and analyzes structure, completeness,
    and basic statistics using pandas.

Usage:
    python pandas_analyst_agent.py --file data.csv --verbose
"""

import os
import logging
import argparse
import uuid
import pandas as pd


class PandasAnalystAgent:
    def __init__(self, name="PandasAnalystAgent", file_path=None):
        self.name = name
        self.agent_id = str(uuid.uuid4())
        self.file_path = file_path
        self.df = None

        if not self.file_path or not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        logging.info(f"[{self.name}] Initialized with ID: {self.agent_id}")

    def load_data(self):
        """Load the dataset from CSV or Excel"""
        ext = os.path.splitext(self.file_path)[-1].lower()
        logging.debug(f"Loading data from: {self.file_path}")

        if ext == ".csv":
            self.df = pd.read_csv(self.file_path)
        elif ext in [".xlsx", ".xls"]:
            self.df = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file type. Use CSV or Excel.")
        logging.info(f"Loaded {len(self.df)} rows and {len(self.df.columns)} columns.")

    def analyze(self):
        """Print dataset metadata and basic insights"""
        if self.df is None:
            raise RuntimeError("Data not loaded.")

        print("\n=== Dataset Overview ===")
        print(f"Shape: {self.df.shape}")
        print("\nColumn Types:\n", self.df.dtypes)

        print("\nMissing Values:\n", self.df.isnull().sum())

        print("\nUnique Values per Column:\n", self.df.nunique())

        print("\nBasic Statistics (Numerical):\n", self.df.describe().T)

    def run_once(self):
        """Perform full data load and analysis"""
        self.load_data()
        self.analyze()


def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def parse_args():
    parser = argparse.ArgumentParser(description="PandasAnalystAgent CLI")
    parser.add_argument("--name", type=str, default="PandasAnalystAgent", help="Agent name")
    parser.add_argument("--file", type=str, required=True, help="Path to CSV or Excel file")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging(args.verbose)

    agent = PandasAnalystAgent(name=args.name, file_path=args.file)
    agent.run_once()


if __name__ == "__main__":
    main()
