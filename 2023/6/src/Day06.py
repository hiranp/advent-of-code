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
            data = file.read().split("\n\n")
        print(f"Using {input_file} for input data.")
    except FileNotFoundError:
        print(f"Input file {input_file} not found. Fetching data from AoC website.")
        puzzle = Puzzle(year=2023, day=6)
        data = puzzle.input_data.split("\n\n")
    return data


def part1(data):
    pass


def part2(data):
    pass


test_data = """
121232141
123124124
"""


if __name__ == "__main__":
    part1_answer = part1(test_data.split("\n\n"))
    print(f"Test 1: {part1_answer}")
    assert part1_answer == None

    data = read_input_data(INPUT_FILE)
    start_p1 = time.perf_counter()
    part1_answer = part1(data)
    print(f"Part 1 answer: {part1_answer}")
    # puzzle.answer_a = part1_answer
    print(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")

    start_p2 = time.perf_counter()
    # part2_answer = part2(data)
    # print(f"Part 2 answer: {part2_answer}")
    # puzzle.answer_b = part2_answer
    print(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
