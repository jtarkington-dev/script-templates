#!/usr/bin/env python3
"""
GPTAgent Template
Author: Jeremy Tarkington
Description:
    A reusable agent that sends user prompts to a GPT model and returns responses.
    Configured for OpenAI or OpenRouter APIs. Easily extended for task automation.

Usage:
    python gpt_agent_template.py --loop --verbose
"""

import os
import uuid
import time
import logging
import argparse
import requests

# Update this to use OpenAI or another provider if needed
DEFAULT_API_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-4-turbo"

class GPTAgent:
    def __init__(self, name="GPTAgent", api_key=None, model=DEFAULT_MODEL):
        self.name = name
        self.agent_id = str(uuid.uuid4())
        self.running = True
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.model = model
        if not self.api_key:
            raise ValueError("No API key provided. Set OPENROUTER_API_KEY in .env or shell.")
        logging.info(f"[{self.name}] Initialized with ID: {self.agent_id}")

    def ask(self, user_prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ]
        }

        logging.debug(f"Sending prompt to {DEFAULT_API_URL}")
        response = requests.post(DEFAULT_API_URL, headers=headers, json=body)

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            logging.info("Response received successfully.")
            return content.strip()
        else:
            logging.error(f"Error from API: {response.status_code} - {response.text}")
            return "[ERROR] Failed to get a response."

    def run_once(self):
        user_prompt = input("You: ")
        logging.info(f"User prompt: {user_prompt}")
        response = self.ask(user_prompt)
        print(f"\n{self.name}: {response}\n")

    def run_loop(self):
        print(f"Starting {self.name} loop mode. Type 'exit' to quit.\n")
        try:
            while self.running:
                user_prompt = input("You: ")
                if user_prompt.strip().lower() in ("exit", "quit"):
                    break
                response = self.ask(user_prompt)
                print(f"\n{self.name}: {response}\n")
        except KeyboardInterrupt:
            self.running = False
            print("\n[Ctrl+C detected. Exiting...]")


def setup_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def parse_args():
    parser = argparse.ArgumentParser(description="GPTAgent CLI")
    parser.add_argument("--name", type=str, default="GPTAgent", help="Agent name")
    parser.add_argument("--loop", action="store_true", help="Run in continuous loop")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="Model to use")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging(args.verbose)

    agent = GPTAgent(name=args.name, model=args.model)

    if args.loop:
        agent.run_loop()
    else:
        agent.run_once()


if __name__ == "__main__":
    main()
