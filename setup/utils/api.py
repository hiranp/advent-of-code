import requests
import os
from os.path import exists
from datetime import datetime

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day
current_directory = os.getcwd()

session_cookie = os.path.join(current_directory, "setup/session.cookie")

def get_session_id(filename):
    if not exists(filename):
        # Handle the error: either create the file or raise an error
        raise FileNotFoundError(f"No such file or directory: '{filename}'")
    with open(filename) as f:
        session_id = ""
        # If starts with session=, remove it
        if f.read().startswith("session="):
            f.seek(8)
        session_id = f.read().strip()
        return session_id

def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"

SESSION = get_session_id(session_cookie)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
COOKIES = {"session": SESSION}


def get_input(day):
    path = f"inputs/{day:02d}"

    if not exists(path):
        url = get_url(current_year, current_day)
        print(f"Downloading input from {url}")
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
