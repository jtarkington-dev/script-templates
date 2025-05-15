#!/bin/bash
# ----------------------------------------
# Script: archive_logs.sh
# Author: Jeremy Tarkington
# Description: Archives all .log files in a folder into a ZIP file.
# Usage: ./archive_logs.sh /path/to/logs /path/to/output/logs_archive.zip
# ----------------------------------------

set -euo pipefail
IFS=$'\n\t'

LOG_DIR="$1"
OUTPUT_ZIP="$2"

if [[ ! -d "$LOG_DIR" ]]; then
  echo "Error: Log directory not found: $LOG_DIR"
  exit 1
fi

TMP_DIR=$(mktemp -d)
find "$LOG_DIR" -type f -name "*.log" -exec cp {} "$TMP_DIR" \;

if compgen -G "$TMP_DIR/*.log" > /dev/null; then
  zip -j "$OUTPUT_ZIP" "$TMP_DIR"/*.log > /dev/null
  echo "Logs archived to: $OUTPUT_ZIP"
else
  echo "No log files to archive in $LOG_DIR"
fi

rm -rf "$TMP_DIR"
