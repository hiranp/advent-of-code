from aocd.models import Puzzle
import re
import os
import time

# Constants
DEBUG = True
INPUT_FILE = "../input.txt"


def debug(*args):
    if DEBUG:
        print(*args)


def read_input_data(input_file):
    """
    Read the input data from the input_file if it exists, or fetch it from the AoC website.

    Parameters:
    input_file (str): The path to the input file.

    Returns:
    data (list): The input data, split by newline characters.
    """
    try:
        cwd = os.path.dirname(os.path.realpath(__file__))
        input_file = f"{cwd}/{input_file}"
        with open(input_file, "r") as file:
            data = file.read()
        debug(f"Using {input_file} for input data.")
    except FileNotFoundError:
        debug(f"Input file {input_file} not found. Fetching data from AoC website.")
        puzzle = Puzzle(year=2023, day=4)
        data = puzzle.input_data
    return data


def part1(data):
    pass


def part2(data):
    pass


tdata1 = """
121232141
123124124
"""


if __name__ == "__main__":
    part1_answer = part1(tdata1.split("\n\n"))
    debug(f"Test 1: {part1_answer}")
    assert part1_answer == None

    data = read_input_data(INPUT_FILE)
    start_p1 = time.perf_counter()
    part1_answer = part1(data)
    debug(f"Part 1 answer: {part1_answer}")
    debug(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")
    # puzzle.answer_a = part1_answer

    # start_p2 = time.perf_counter()
    # part2_answer = part2(data)
    # debug(f"Part 2 answer: {part2_answer}")\
    # debug(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
    # puzzle.answer_b = part2_answer
