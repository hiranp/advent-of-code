from operator import ge
import os
from os.path import exists
from datetime import datetime
import urllib.request
import http.cookiejar
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.recording = 0
    self.data = ''

  def handle_starttag(self, tag, attrs):
    if tag == 'article':
      for name, value in attrs:
        if name == 'class' and value == 'day-desc':
          self.recording += 1
    if tag == 'h2' and self.recording:
      self.recording += 1

  def handle_endtag(self, tag):
    if tag == 'h2' and self.recording:
      self.recording -= 1
    if tag == 'article' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording == 2:
      self.data = data

def extract_h2_text(url):
  # Send a GET request to the URL
  with urllib.request.urlopen(url) as response:
    html = response.read().decode()

  # Parse the HTML content of the page with HTMLParser
  parser = MyHTMLParser()
  parser.feed(html)

  return parser.data

# Use the function
url = 'https://adventofcode.com/2023/day/3'
print(extract_h2_text(url))

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day
current_directory = os.getcwd()

def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"

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

    # Create a cookie jar and add the session cookie
    cookie_jar = http.cookiejar.CookieJar()
    HEADERS = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    SESSION = 112233445566778899
    cookie = http.cookiejar.Cookie(version=0, name='session', value=SESSION, port=None, port_specified=False, domain='adventofcode.com', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=True, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
    cookie_jar.set_cookie(cookie)

    # Create an opener that will use the cookie jar
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

    # Add the User-Agent header
    opener.addheaders = [('User-Agent', HEADERS['User-Agent'])]

    # Use the opener to make the request
    response = opener.open(url)

    # Check the response status
    if response.status != 200:
      raise RuntimeError(f"Request failed\n\tstatus code: {response.status}\n\tmessage: {response.read().decode()}")

    # Write the response content to the file
    with open(input_file, "w") as f:
      f.write(response.read().decode()[:-1])

  with open(input_file, "r") as f:
    return f.read()
  
# Get the session cookie

print(f"Generate input for {current_year}/{current_day:01d}")
get_input(current_day)
