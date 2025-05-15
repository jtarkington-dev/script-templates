#!/bin/bash
# ----------------------------------------
# Script: backup_folder.sh
# Author: Jeremy Tarkington
# Description: Backups a folder to a destination with a timestamped subfolder.
# Usage: ./backup_folder.sh /source/folder /destination/backups
# ----------------------------------------

set -euo pipefail
IFS=$'\n\t'

SOURCE="$1"
DEST_ROOT="$2"

if [[ ! -d "$SOURCE" ]]; then
  echo "Error: Source directory not found: $SOURCE"
  exit 1
fi

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
DEST="$DEST_ROOT/backup_$TIMESTAMP"

mkdir -p "$DEST"
cp -r "$SOURCE"/* "$DEST"

echo "Backup completed to: $DEST"
