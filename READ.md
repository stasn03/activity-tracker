Overview

The Activity Tracker is a Python script that logs user activity, including:

    Active window changes (e.g., switching between applications).

    Keystrokes (e.g., keys pressed by the user).

    The logs are saved to a text file in the logs/ directory, organized by date.
Features:

    Window Tracking: Logs the title of the active window whenever it changes.

    Keystroke Logging: Logs every key pressed by the user.

    Daily Logs: Saves logs to a new file each day in the logs/ directory.

    Quits the program if f12 is pressed.

    Cross-Platform: Works on Windows, macOS, and Linux (requires pygetwindow and pynput).

Installation Prerequisites

    Python 3.x

    pynput library (for keyboard input).

    pygetwindow library (for tracking active windows).