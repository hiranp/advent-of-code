from operator import ge
import os
from os.path import exists
from datetime import datetime
import urllib.request
import http.cookiejar
from html.parser import HTMLParser


# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day
current_directory = os.getcwd()


class AocPageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.recording = 0
        self.data = ""

    def handle_starttag(self, tag, attrs):
        if tag == "article":
            for name, value in attrs:
                if name == "class" and value == "day-desc":
                    self.recording += 1
        if tag == "h2" and self.recording:
            self.recording += 1

    def handle_endtag(self, tag):
        if tag == "h2" and self.recording:
            self.recording -= 1
        if tag == "article" and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording == 2:
            self.data = data


def extract_h2_text(url):
    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()

    # Parse the HTML content of the page with HTMLParser
    parser = AocPageParser()
    parser.feed(html)

    # Extract the title after Day X: from the data
    title = parser.data = parser.data.split(": ")[1]
    # Remove the trailing --- from the title
    title = title[:-3].strip()

    return title


# Use the function
url = f"https://adventofcode.com/{current_year}/day/{current_day}"
print(extract_h2_text(url))
