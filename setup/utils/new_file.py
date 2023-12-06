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
with open(f"{current_year}/{current_day}/src/Day{current_day:01d}.kt", "r") as f:
    DEFAULT_KT = f.read()

with open(f"{current_year}/{current_day}/src/Utils.kt", "r") as f:
    DEFAULT_KT_UTL = f.read()

# Go template
DEFAULT_GO = """
package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "strings"
)

func main() {
    data, err := ioutil.ReadFile("input.txt")
    if err != nil {
        log.Fatal(err)
    }

    input := strings.Split(string(data), "\\n")

    fmt.Println(part1(input))
    fmt.Println(part2(input))
}

func() part1(input []string) int {
    return 0
}

func() part2(input []string) int {
    return 0
}
"""

DEFAULT_GO_MOD = f"""
module github.com/hiranp/advent-of-code/{current_year}/{current_day}

go 1.20
"""

with open(f"{current_year}/{current_day}/src/Day{current_day:01d}.go", "r") as f:
    DEFAULT_GO = f.read()
with open(f"{current_year}/{current_day}/go.mod", "r") as f:
    DEFAULT_GO_MOD = f.read()


# Python template
DEFAULT_PY = f"""
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

path = f"{current_year}/{current_day}/src/solver{current_day}.py"

# Create the file if it doesn't exist
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write(DEFAULT_PY)

print(f"Enter your solution in {path}")
