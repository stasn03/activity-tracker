# Activity Tracker

This project tracks keyboard activity and logs the keys pressed along with the active window context (the application or window the user is interacting with). It stores the captured data in a PostgreSQL database for later analysis.

## Features

- Captures keyboard activity and logs the pressed keys.
- Records the active window title to correlate key presses with the application the user is using.
- Stores the data securely in a PostgreSQL database.
- Stops capturing when a specific key (F12) is pressed.

## Technologies Used

- **Python** - Programming language used to develop the activity tracker.
- **PostgreSQL** - Database used to store the tracked data.
- **pynput** - Library for monitoring and controlling input devices.
- **pygetwindow** - Library to retrieve the active window's title.
- **psycopg2** - Library for PostgreSQL database interaction.

## Prerequisites

Before running this project, ensure that you have the following installed:

- Python 3.x
- PostgreSQL database running and accessible
- Required Python libraries:
  - `pynput`
  - `pygetwindow`
  - `psycopg2`

To install the required libraries, run:

```bash
pip install pynput 
pip install pygetwindow 
pip install psycopg2
```

### Setup
1. Clone this repository:
```bash
git clone "https://github.com/stasn03/activity-tracker.git"
```
2. Setup your own PostgreSQL database and table;

### Running the Program
To start the program is enough to run the following program:
``` bash
python script.py
```
