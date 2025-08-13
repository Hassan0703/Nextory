import schedule
import time
import random
from pathlib import Path
from core.utils import append_feature
from core.github_api import commit_change

FEATURES_FILE = Path(__file__).resolve().parent.parent / "features" / "features.txt"

def schedule_commits(settings):
    def job():
        append_feature(FEATURES_FILE)
        commit_change(
            settings["github_token"],
            settings["repo_name"],
            "features/features.txt",
            "Automated commit from Nextory"
        )

    # Schedule one commit for each hour at a random minute
    for hour in range(0, 24):  # You can change to (9, 22) for 9 AM to 9 PM
        minute = str(random.randint(0, 59)).zfill(2)
        hour_str = str(hour).zfill(2)
        schedule.every().day.at(f"{hour_str}:{minute}").do(job)

    print("📅 Scheduler started... Commits will run once randomly within each hour.")
    while True:
        schedule.run_pending()
        time.sleep(30)

def random_time_str():
    import random
    h = str(random.randint(9, 21)).zfill(2)
    m = str(random.randint(0, 59)).zfill(2)
    return f"{h}:{m}"
