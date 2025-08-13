import requests
import os
import base64
from requests.exceptions import RequestException

BASE_URL = "https://api.github.com"

def create_repo(token, repo_name, private=False):
    """
    Create a new GitHub repository or confirm if it already exists.
    Returns True if the repo exists or was created successfully, False otherwise.
    """
    try:
        username = get_username(token)

        # Check if repo already exists
        check_url = f"{BASE_URL}/repos/{username}/{repo_name}"
        check_resp = requests.get(check_url, headers={"Authorization": f"token {token}"}, timeout=10)
        if check_resp.status_code == 200:
            print(f"ℹ Repository '{repo_name}' already exists.")
            return True

        # Create the repository
        url = f"{BASE_URL}/user/repos"
        headers = {"Authorization": f"token {token}"}
        data = {"name": repo_name, "auto_init": True, "private": private}

        response = requests.post(url, json=data, headers=headers, timeout=10)
        if response.status_code == 201:
            print(f"✅ Repository '{repo_name}' created successfully.")
            return True
        else:
            print(f"❌ Failed to create repo: {response.status_code} - {response.text}")
            return False

    except RequestException as e:
        print(f"❌ Network error while creating repo: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def commit_change(token, repo_name, file_path, commit_message):
    """Commit a file to the GitHub repository."""
    if not os.path.isfile(file_path):
        print(f"❌ File '{file_path}' not found.")
        return False

    try:
        username = get_username(token)
        headers = {"Authorization": f"token {token}"}

        # Get file SHA if exists
        url = f"{BASE_URL}/repos/{username}/{repo_name}/contents/{file_path}"
        get_resp = requests.get(url, headers=headers, timeout=10)
        sha = get_resp.json().get("sha") if get_resp.status_code == 200 else None

        # Encode file content
        with open(file_path, "rb") as f:
            content_encoded = base64.b64encode(f.read()).decode("utf-8")

        data = {"message": commit_message, "content": content_encoded}
        if sha:
            data["sha"] = sha  # Include SHA for updates

        put_resp = requests.put(url, json=data, headers=headers, timeout=10)

        if put_resp.status_code in [200, 201]:
            print(f"✅ Commit pushed: {commit_message}")
            return True
        else:
            print(f"❌ Commit failed: {put_resp.status_code} - {put_resp.text}")
            return False

    except RequestException as e:
        print(f"❌ Network error while committing changes: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def get_username(token):
    """Retrieve GitHub username using the token."""
    try:
        headers = {"Authorization": f"token {token}"}
        resp = requests.get(f"{BASE_URL}/user", headers=headers, timeout=10)
        if resp.status_code != 200:
            raise Exception(f"GitHub API error: {resp.status_code} - {resp.text}")
        return resp.json()["login"]
    except RequestException as e:
        raise Exception(f"❌ Failed to fetch username: {e}")
