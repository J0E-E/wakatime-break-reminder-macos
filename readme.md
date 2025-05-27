# WakaTime Break Reminder

**WakaTime Break Reminder** is a lightweight utility that monitors your [WakaTime](https://wakatime.com/) log file and notifies you when it’s time to take a break. It tracks your coding time and sends desktop notifications at configurable intervals.

##  Features

-  Tracks productive time using WakaTime’s status bar updates  
-  Sends native macOS notifications via `terminal-notifier`  
-  Configurable milestone and polling intervals  
-  Prevents duplicate alerts for the same milestone  

##  Installation

1. **Clone or download this repository:**

   ```bash
   git clone https://github.com/J0E-E/wakatime-break-reminder-macos.git
   cd wakatime-break-reminder-macos
   ```

2. **Install dependencies:**

   WakaBreak requires [`terminal-notifier`](https://github.com/julienXX/terminal-notifier), which is available via Homebrew:

   ```bash
   brew install terminal-notifier
   ```

3. **(Optional) Make the script executable:**

   ```bash
   chmod +x wakatime-break-reminder.py
   ```

## Usage

Run the script using Python 3:

```bash
python3 wakatime-break-reminder.py --log ~/.wakatime/macos-wakatime.log
```

### Command-Line Arguments

| Argument       | Description                                                  | Default |
|----------------|--------------------------------------------------------------|---------|
| `--log`        | Path to your WakaTime log file (required)                    | N/A     |
| `--milestone`  | Milestone interval in minutes to trigger reminders           | 100     |
| `--poll`       | Polling interval in seconds to check the log file            | 5       |

### Example:

```bash
python wakatime-break-reminder.py --log ~/.wakatime/macos-wakatime.log --milestone 60 --poll 3
```

This command checks the WakaTime log every 3 seconds and sends a reminder every 60 minutes of logged activity.

## Running Automatically on macOS Startup

You can run WakaTime Break Reminder automatically in the background at login using a simple script.

1. **Create a shell script:**

   Create a file named `start_wakatime_break_reminder.command`:

   ```bash
   #!/bin/bash
   /usr/bin/python3 /path/to/wakatime-break-reminder.py --log ~/.wakatime/macos-wakatime.log --milestone 100 &
   ```

   Replace `/path/to/wakatime-break-reminder.py` with the full path to the script.

2. **Make the script executable:**

   ```bash
   chmod +x start_wakatime_break_reminder.command
   ```

3. **Add to macOS Login Items:**

   - Open **System Settings > General > Login Items**
   - Click the ➕ button and add your `start_wakatime_break_reminder.command` script.

   Alternatively, advanced users can create a `launchd` job for persistent background execution.

## Requirements

- macOS (due to `terminal-notifier`)
- WakaTime installed and logging to the status bar
- Python 3