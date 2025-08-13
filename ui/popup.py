import json
import os
import sys
from pathlib import Path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

CONFIG_FILE = resource_path(os.path.join("config", "settings.json"))

def welcome_message():
    print("=" * 50)
    print("🚀 Welcome to Nextory — Automated GitHub Commits Tool")
    print("Developed by Nextash")
    print("=" * 50)

def get_user_settings():
    with open(CONFIG_FILE, "r") as f:
        settings = json.load(f)

    if not settings["github_token"]:
        settings["github_token"] = input("Enter your GitHub Personal Access Token: ").strip()

    if not settings["repo_name"]:
        settings["repo_name"] = input("Enter the repository name to use/create: ").strip()

    with open(CONFIG_FILE, "w") as f:
        json.dump(settings, f, indent=4)

    return settings
