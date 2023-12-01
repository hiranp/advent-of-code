import os
from datetime import datetime

# Get the current year
current_year = datetime.now().year

path = f"{current_year}/src/"

# Create the path if it doesn't exist
if not os.path.exists(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
l = filter(lambda x: "__" not in x and ".py" in x, os.listdir(f"{current_year}/src"))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1



DEFAULT_FILE = f"from utils.api import get_input\n\ninput_str = get_input({n})\n\n# WRITE YOUR SOLUTION HERE\n\n"

path = f"{current_year}/src/{n:02d}.py"
    
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
