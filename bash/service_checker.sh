#!/bin/bash
# ----------------------------------------
# Script: service_checker.sh
# Author: Jeremy Tarkington
# Description: Checks if a systemd service is active and restarts it if not.
# Usage: ./service_checker.sh nginx
# ----------------------------------------

set -euo pipefail
IFS=$'\n\t'

SERVICE_NAME="$1"

if ! systemctl list-units --type=service | grep -q "$SERVICE_NAME"; then
  echo "Error: Service '$SERVICE_NAME' not found."
  exit 1
fi

STATUS=$(systemctl is-active "$SERVICE_NAME")

if [[ "$STATUS" != "active" ]]; then
  echo "Service '$SERVICE_NAME' is not running. Attempting to restart..."
  sudo systemctl restart "$SERVICE_NAME"
  echo "Service restarted."
else
  echo "Service '$SERVICE_NAME' is running."
fi
