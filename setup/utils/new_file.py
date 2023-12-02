import os
import re

from datetime import datetime
from api import get_input

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day

path = f"{current_year}/{current_day}/src"

# Create the path if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)

# Get the next number for the file
files = [x for x in os.listdir(path) if "__" not in x and x.endswith('.py')]
if files:
    match = re.search(r'(\d+)\.py$', files[-1])
    n = int(match.group(1)) + 1 if match is not None else 1
else:
    n = 1
    
# Generated the input file
input_str = get_input(current_day)
with open(f"{current_year}/{current_day}/input.txt", "w") as f:
    f.write(input_str)
    
# Copy contents of template file
DEFAULT_FILE = f"""
from aocd.models import Puzzle
import re

puzzle = Puzzle(year={current_year}, day={current_day})
data = puzzle.input_data
# print(data)

def part1(data):
    pass    

def part2(data):
    pass

part1_answer = part1(data)
print(f"Part 1 answer: {{part1_answer}}")

# puzzle.answer_a = part1_answer

# part2_answer = part2(data)
# print(f"Part 2 answer: {{part2_answer}}")
# puzzle.answer_b = part2_answer
"""
# with open("python_templ.py", "r") as f:
#     DEFAULT_FILE = f.read()

path = f"{current_year}/{current_day}/src/solver.py"

# Create the file if it doesn't exist
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
