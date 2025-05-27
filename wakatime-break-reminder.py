import re
import time
import subprocess
from pathlib import Path
import argparse

# === CLI ARGUMENTS ===
parser = argparse.ArgumentParser(description="Break reminder based on Wakatime log.")
parser.add_argument(
    "--log",
    type=Path,
    required=True,
    help="Path to the wakatime log file (e.g., ~/.wakatime/macos-wakatime.log)",
)
parser.add_argument(
    "--milestone",
    type=int,
    default=100,
    help="Milestone interval in minutes to trigger a reminder (default: 100)",
)
parser.add_argument(
    "--poll",
    type=int,
    default=5,
    help="Polling interval in seconds to check the log file (default: 5)",
)
args = parser.parse_args()

# === CONFIG ===
log_path = args.log.expanduser().resolve()
milestone_interval = args.milestone
poll_interval = args.poll
seen_alerts = set()
regex = re.compile(r"Set status bar text:\s*(\d+)\s*hrs?\s*(\d+)?\s*mins?")


def minutes_total(hr: int, mins: int) -> int:
    print(f"{hr} hrs, {mins} mins")
    return hr * 60 + mins


def notify(message: str):
    print(f"NOTIFY: {message}")
    subprocess.run([
        "terminal-notifier",
        "-title", "Break Reminder",
        "-message", message,
        "-sound", "default",
    ])


print(f"Monitoring log at {log_path}... (Milestone every {milestone_interval} mins)")

with open(log_path, "r") as file:
    next_milestone = milestone_interval
    file.seek(0, 2)  # Seek to end of file
    while True:
        line = file.readline()
        if not line:
            time.sleep(poll_interval)
            continue

        match = regex.search(line)
        if match:
            hr = int(match.group(1))
            mins = int(match.group(2) or 0)
            total = minutes_total(hr, mins)
            print(f"Total: {total}, Next Milestone: {next_milestone}")

            # Within 10 mins before or after the milestone
            if next_milestone - 10 <= total and next_milestone not in seen_alerts:
                notify(f"You've worked for {total} minutes. Time for a break!")
                seen_alerts.add(next_milestone)
                next_milestone += milestone_interval