import random
import datetime

def get_random_times_per_day(times_per_day):
    now = datetime.datetime.now()
    times = []
    for _ in range(times_per_day):
        hour = random.randint(9, 21)  # Between 9 AM and 9 PM
        minute = random.randint(0, 59)
        run_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if run_time < now:
            run_time += datetime.timedelta(days=1)
        times.append(run_time)
    return sorted(times)

def append_feature(file_path):
    with open(file_path, "a") as f:
        f.write(f"- New feature added at {datetime.datetime.now()}\n")
