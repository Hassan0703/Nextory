from ui.popup import welcome_message, get_user_settings
from core.github_api import create_repo
from core.scheduler import schedule_commits
import sys
import traceback

def safe_exit(message, exit_code=1):
    """Print error message and exit gracefully."""
    print(f"❌ {message}")
    sys.exit(exit_code)

if __name__ == "__main__":
    try:
        welcome_message()
        settings = get_user_settings()

        # Basic validation
        if not settings.get("github_token") or not settings.get("repo_name"):
            safe_exit("GitHub token and repository name are required.")

        print("🔍 Validating inputs...")
        if len(settings["github_token"]) < 10:
            safe_exit("Invalid GitHub token. Please check and try again.")

        # Create repository
        print(f"📦 Creating or accessing repository '{settings['repo_name']}'...")
        if not create_repo(settings["github_token"], settings["repo_name"]):
            safe_exit(f"Could not create or access repository '{settings['repo_name']}'.")

        # Start scheduler
        schedule_commits(settings)

    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user. Exiting...")
        sys.exit(0)

    except Exception as e:
        print("\n🔥 An unexpected error occurred!")
        traceback.print_exc()
        safe_exit(str(e))
