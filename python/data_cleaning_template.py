#!/usr/bin/env python3
"""
data_cleaning_template.py
Author: Jeremy Tarkington

Reusable data cleaning script with:
- CSV loading
- Column normalization
- Null handling
- Type conversion
- Export to cleaned CSV
"""

import pandas as pd
import argparse
import logging
import sys
import os


# ========== Logging ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# ========== Data Cleaning Steps ==========
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting data cleaning...")

    # Normalize column names
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w]", "", regex=True)
    )

    # Drop entirely empty columns
    df.dropna(axis=1, how="all", inplace=True)

    # Fill missing values (example: fill with 0 or forward fill)
    df.fillna(method="ffill", inplace=True)

    # Convert columns to proper dtypes (optional example)
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                continue

    logging.info("Cleaning complete.")
    return df


# ========== Main Logic ==========
def main(input_file, output_file):
    if not os.path.exists(input_file):
        logging.error(f"Input file not found: {input_file}")
        sys.exit(1)

    df = pd.read_csv(input_file)
    logging.info(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")

    cleaned_df = clean_dataframe(df)
    cleaned_df.to_csv(output_file, index=False)

    logging.info(f"Cleaned data written to: {output_file}")


# ========== CLI ==========
def parse_args():
    parser = argparse.ArgumentParser(description="Clean a CSV file and export the result.")
    parser.add_argument("--input", required=True, help="Path to raw CSV")
    parser.add_argument("--output", required=True, help="Path to save cleaned CSV")
    return parser.parse_args()


# ========== Entrypoint ==========
if __name__ == "__main__":
    args = parse_args()
    try:
        main(args.input, args.output)
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")
        sys.exit(1)
