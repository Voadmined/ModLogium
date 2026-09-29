import json
import os
import sys


if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "data", "logs.json")


def load_logs():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            logs = json.load(file)
            return logs
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_logs(logs):
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(logs, file, indent=4)
        return True

    except Exception as e:
        return False