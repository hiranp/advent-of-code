import os
from datetime import datetime

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().strftime('%d')

base_link = "https://github.com/hiranp/advent-of-code/blob/main/"

def parse(e):
    name = e.replace(".py", "")
    # name = " ".join(name.split("_")[1:])
    return f"[{name}]({base_link}{e})"

path = f"{current_year}/{current_day}/src"

# Create the path if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)
    
solutions = filter(lambda x: ".py" in x and "init" not in x, os.listdir(path))

readme_content = "# Advent of code\nProblems list:\n"
tmp = [f"{i+1}. {parse(e)}" for i, e in enumerate(sorted(solutions))]
readme_content += "\n".join(tmp)

with open("README.md", "w") as f:
    f.write(
        readme_content
        + "\n\nCreated via: [advent-of-code-setup](https://github.com/tomfran/advent-of-code-setup)"
    )
