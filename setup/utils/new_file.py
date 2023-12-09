import os
import re

from datetime import datetime
from api import get_input

# Get the current year and day
current_year = datetime.now().year
current_day = datetime.now().day

cwd = os.path.dirname(os.path.realpath(__file__))
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

path = f"{current_year}/{current_day}/src/Day{current_day:02d}.py"

# Create the file if it doesn't exist
if not os.path.exists(path):
    with open(f"{cwd}/tmpl.py", "r") as tmpl:
        DEFAULT_PY = tmpl.read()
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
# Create the file if it doesn't exist
kortlin_tpl = f"{current_year}/{current_day}/src/Day{current_day:02d}.kt"
if not os.path.exists(kortlin_tpl):
    with open(kortlin_tpl, "w") as f:
        f.write(DEFAULT_KT)
    with open(f"{current_year}/{current_day}/src/Utils.kt", "w") as f:
        f.write(DEFAULT_KT_UTL)

# Go starter template
DEFAULT_GO_MOD = f"""
module github.com/hiranp/advent-of-code/{current_year}/{current_day}

go 1.20
"""
with open(f"{cwd}/tmpl.go", "r") as tmpl:
    DEFAULT_GO = tmpl.read()
# Create the file if it doesn't exist
go_tpl = f"{current_year}/{current_day}/src/Day{current_day:02d}.go"
if not os.path.exists(go_tpl):
    with open(go_tpl, "w") as f:
        f.write(DEFAULT_GO)
    with open(f"{current_year}/{current_day}/go.mod", "w") as f:
        f.write(DEFAULT_GO_MOD)
# Add entry to the end of go.work file
mod_path = f"use ./{current_year}/{current_day}"
# Only add mod_path if it doesn't exist in go.work
with open("go.work", "r") as f:
    if not mod_path in f.read():
        with open("go.work", "a") as f:
            f.write(f"\n{mod_path}\n")


print(f"Enter your solution in {path}")
