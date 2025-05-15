#!/usr/bin/env python3
"""
api_request_template.py
Author: Jeremy Tarkington

Reusable REST API caller with:
- Base URL + endpoint separation
- Optional headers + API keys
- Built-in retry logic
- Logging and error handling
"""

import requests
import time
import logging


# ========== Logging ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# ========== API Client Logic ==========
def call_api(
    method="GET",
    base_url="https://jsonplaceholder.typicode.com",
    endpoint="/posts/1",
    headers=None,
    params=None,
    payload=None,
    retries=3,
    timeout=5
):
    url = f"{base_url.rstrip('/')}{endpoint}"

    for attempt in range(1, retries + 1):
        try:
            logging.info(f"[{method}] {url} (Attempt {attempt})")

            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=payload,
                timeout=timeout
            )

            response.raise_for_status()
            logging.info(f"Status: {response.status_code}")
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(2 ** attempt)
            else:
                logging.error("Max retries reached. Giving up.")
                return None


# ========== Example Usage ==========
if __name__ == "__main__":
    headers = {
        "Accept": "application/json",
        # "Authorization": "Bearer YOUR_API_KEY"
    }

    data = call_api(
        method="GET",
        endpoint="/posts/2",
        headers=headers
    )

    if data:
        print("\n=== API Response ===")
        print(data)
