import os
from datetime import datetime
from api import get_input

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day

path = f"{current_year}/{current_day}/src"

# Create the path if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)
    
l = filter(lambda x: "__" not in x and ".py" in x, os.listdir(path))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

# Generated the input file
input_str = get_input(n)
with open(f"{current_year}/{current_day}/input.txt", "w") as f:
    f.write(input_str)
    
# Copy contents of template file
DEFAULT_FILE = ""
with open("python_templ.py", "r") as f:
    DEFAULT_FILE = f.read()

path = f"{current_year}/{current_day}/src/{n:02}.py"
    
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
