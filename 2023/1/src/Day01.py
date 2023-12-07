from aocd.models import Puzzle
import re
import os
import time

# Constants
INPUT_FILE = "../input.txt"


def read_input_data(input_file):
    try:
        cwd = os.path.dirname(os.path.realpath(__file__))
        input_file = f"{cwd}/{input_file}"
        with open(input_file, "r") as file:
            data = file.read().split("\n")
        print(f"Using {input_file} for input data.")
    except FileNotFoundError:
        print(f"Input file {input_file} not found. Fetching data from AoC website.")
        puzzle = Puzzle(year=2023, day=6)
        data = puzzle.input_data.split("\n")
    return data


word_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part1(input):
    total = 0
    # 1. Find first and last digit of each number
    # 2. Sum all numbers
    # 3. Return the sum

    for x in range(0, len(input)):
        digits = [ch for ch in input[x] if ch.isdigit()]
        # print(digits)
        if digits:  # Check if digits is not empty
            total += int(digits[0] + digits[-1])
    return total


def check_digits(input):
    val = ""
    if input in word_to_num:
        val = word_to_num[input]
        # print(f"Found {input} = {val}")
        return str(val)
    return str(input)


def part2(lines):
    total = 0
    spliter = "(?=(" + "|".join(word_to_num.keys()) + "|\\d))"
    for line in lines:
        digits = [*map(check_digits, re.findall(spliter, line))]
        if digits:
            # print(f"Digits: {digits}")
            total += int(digits[0] + digits[-1])
    return total

test_data1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_data2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

if __name__ == "__main__":
    t_data = test_data1.split("\n")
    print(t_data)
    part1_answer = part1(t_data)
    print(f"Test 1: {part1_answer}")
    assert part1_answer == 142
    
    t_data = test_data2.split("\n")
    part2_answer = part2(t_data)
    print(f"Test 2: {part2_answer}")
    assert part2_answer == 281

    data = read_input_data(INPUT_FILE)

    start_p1 = time.perf_counter()
    part1_answer = part1(data)
    print(f"Part 1 answer: {part1_answer}")
    # puzzle.answer_a = part1_answer
    print(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")

    start_p2 = time.perf_counter()
    part2_answer = part2(data)
    print(f"Part 2 answer: {part2_answer}")
    print(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
    # puzzle.answer_b = part2_answer
   
