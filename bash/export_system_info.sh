#!/bin/bash
# ----------------------------------------
# Script: export_system_info.sh
# Author: Jeremy Tarkington
# Description: Exports basic system info to a file.
# Usage: ./export_system_info.sh /path/to/output.txt
# ----------------------------------------

set -euo pipefail
IFS=$'\n\t'

OUTPUT_FILE="$1"

{
  echo "Date: $(date)"
  echo "Hostname: $(hostname)"
  echo "User: $(whoami)"
  echo "Uptime: $(uptime -p)"
  echo "CPU Info:"
  lscpu | grep -E '^Model name|^CPU\(s\)'
  echo "Memory Info:"
  free -h
  echo "Disk Usage:"
  df -h
} > "$OUTPUT_FILE"

echo "System info written to: $OUTPUT_FILE"
