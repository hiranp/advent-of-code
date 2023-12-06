import requests
import os
from os.path import exists
from datetime import datetime

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day
current_directory = os.getcwd()

print(f"Current directory is {current_directory}")

def get_session_id():
    # Check if the session cookie exists in environment variable, otherwise use the file
    if "AOC_SESSION" in os.environ:
        session_id = os.environ["AOC_SESSION"]
    else:
        session_cookie_file = os.path.join(current_directory, "setup/session.cookie")
        if not exists(session_cookie_file):
            # Handle the error: either create the file or raise an error
            raise FileNotFoundError(f"No such file or directory: '{session_cookie_file}'")
        with open(session_cookie_file) as f:
            session_id = ""
            # If starts with session=, remove it
            if f.read().startswith("session="):
                f.seek(8)
            session_id = f.read().strip()
    return session_id

def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"

SESSION = get_session_id()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
COOKIES = {"session": SESSION}


def get_input(day):
    input_file = f"{current_year}/{day:01d}/input.txt"
    path = os.path.join(current_directory, f"{current_year}/{day:01d}")

    # Create the path if it doesn't exist
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        
    # Check if the file exists before trying to open it
    if not os.path.exists(input_file):
        url = get_url(current_year, current_day)
        print(f"Downloading input from {url}")
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(input_file, "w") as f:
            f.write(response.text[:-1])

    with open(input_file, "r") as f:
        return f.read()