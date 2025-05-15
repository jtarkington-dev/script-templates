#!/bin/bash
# ----------------------------------------
# Script: delete_old_files.sh
# Author: Jeremy Tarkington
# Description: Deletes files older than a specified number of days in a given directory.
# Usage: ./delete_old_files.sh /path/to/folder 30
# ----------------------------------------

set -euo pipefail
IFS=$'\n\t'

# === INPUT ===
TARGET_DIR="$1"
DAYS_OLD="$2"

# === CHECKS ===
if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Error: Directory does not exist: $TARGET_DIR"
  exit 1
fi

echo "Deleting files older than $DAYS_OLD days from $TARGET_DIR..."
find "$TARGET_DIR" -type f -mtime +"$DAYS_OLD" -print -delete
echo "Cleanup complete."
