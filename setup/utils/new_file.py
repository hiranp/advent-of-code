import os
import re

from datetime import datetime
from api import get_input

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day
# current_day = 5

path = f"{current_year}/{current_day}/src"

# Create the path if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)

# Get the next number for the file
files = [x for x in os.listdir(path) if "__" not in x and x.endswith(".py")]
if files:
    match = re.search(r"(\d+)\.py$", files[-1])
    n = int(match.group(1)) + 1 if match is not None else 1
else:
    n = 1

# Generated the input file
input_str = get_input(current_day)
with open(f"{current_year}/{current_day}/input.txt", "w") as f:
    f.write(input_str)

# Copy contents of template file

# Python template
DEFAULT_PY = f"""
from aocd.models import Puzzle
import re
import os

def part1(data):
    pass    

def part2(data):
    pass

if __name__ == "__main__":
    # If the input file is readable, use it instead of the default input data
    current_directory = os.getcwd()
    if os.access(f"{{current_directory}}/../input.txt", os.R_OK):
        with open(f"{{current_directory}}/../input.txt", "r") as file:
            data = file.read().split("\n")
        print("Using input.txt for input data.")
    else:
        # If the input file is not readable, use the default input data
        puzzle = Puzzle(year=2023, day=4)
        data = puzzle.input_data.split("\n")
        
    part1_answer = part1(data)
    print(f"Part 1 answer: {{part1_answer}}")

    # puzzle.answer_a = part1_answer

    # part2_answer = part2(data)
    # print(f"Part 2 answer: {{part2_answer}}")
    # puzzle.answer_b = part2_answer
"""

path = f"{current_year}/{current_day}/src/Day{current_day:01d}.py"

# Create the file if it doesn't exist
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write(DEFAULT_PY)


# Kotlin template
DEFAULT_KT_UTL = """
import java.math.BigInteger
import java.security.MessageDigest
import kotlin.io.path.Path
import kotlin.io.path.readLines

/**
 * Reads lines from the given input txt file.
 */
fun readInput(name: String) = Path("src/$name.txt").readLines()

/**
 * Converts string to md5 hash.
 */
fun String.md5() = BigInteger(1, MessageDigest.getInstance("MD5").digest(toByteArray()))
    .toString(16)
    .padStart(32, '0')

/**
 * The cleaner shorthand for printing output.
 */
fun Any?.println() = println(this)
"""

DEFAULT_KT = """
fun main() {
    fun part1(input: List<String>): Int {
        return input.size
    }

    fun part2(input: List<String>): Int {
        return input.size
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("test")
    check(part1(testInput) == 1)

    val input = readInput("input")
    part1(input).println()
    part2(input).println()
}
"""
with open(f"{current_year}/{current_day}/src/Day{current_day:01d}.kt", "w") as f:
    f.write(DEFAULT_KT)
with open(f"{current_year}/{current_day}/src/Utils.kt", "w") as f:
    f.write(DEFAULT_KT_UTL)

# Go starter template
DEFAULT_GO_MOD = f"""
module github.com/hiranp/advent-of-code/{current_year}/{current_day}

go 1.20
"""
with open("tmpl.go", "r") as tmpl:
    DEFAULT_GO = tmpl.read()
with open(f"{current_year}/{current_day}/src/Day{current_day:01d}.go", "w") as f:
    f.write(DEFAULT_GO)
with open(f"{current_year}/{current_day}/go.mod", "w") as f:
    f.write(DEFAULT_GO_MOD)
# Add entry to the end of go.work file
mod_path = f"use ./{current_year}/{current_day}"
# Only add mod_path if it doesn't exist in go.work
with open("go.work", "r") as f:
    if not mod_path in f.read():
        with open("go.work", "a") as f:
            f.write(f"\n{mod_path}")


print(f"Enter your solution in {path}")
