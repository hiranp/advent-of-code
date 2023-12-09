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


def parse_input(input_data):
    return [
        [int(num) for num in line.split()] for line in input_data.split("\n") if line
    ]


def part1(data):
    histories = parse_input(data)
    return sum(
        extrapolate_next_value(generate_sequences(history)) for history in histories
    )


def extrapolate_next_value(sequences):
    sequences[-1].append(sequences[-1][-1])
    # debug(f"extrapolate_next_value: {sequences}")
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
        debug(f"extrapolate_next_value: {sequences}")
    return sequences[0][-1]


# def generate_sequences(history):
#     sequences = [history]
#     debug(f"generate_sequences: {sequences}")
#     while sequences[-1][0] != 0:
#         sequences.append(
#             [
#                 sequences[-1][i] - sequences[-1][i - 1]
#                 for i in range(1, len(sequences[-1]))
#             ]
#         )
#         sequences[-1].insert(0, 0)
#     return sequences


"""
--- Part Two ---
1. Modify `generate_sequences` to generate sequences until all differences are zero.
2. Modify `extrapolate_next_value` to add a zero at the beginning of the last sequence and fill in new first values for each previous sequence.
3. In `part2`, sum the extrapolated values for each history.

"""


# def generate_sequences2(history):
#     sequences = [history]
#     debug(f"generate_sequences2: {sequences}")
#     try:
#         while not all(x == 0 for x in sequences[-1]):
#             sequences.append(
#                 [
#                     seq2 - seq1
#                     for seq1, seq2 in zip(sequences[-1][:-1], sequences[-1][1:])
#                 ]
#             )
#     except ValueError:
#         # Skip lines that cannot be converted to integers
#         pass
#     return sequences


def generate_sequences(history, until_zero=False):
    sequences = [history]
    while True:
        sequences.append(
            [seq2 - seq1 for seq1, seq2 in zip(sequences[-1][:-1], sequences[-1][1:])]
        )
        debug(f"generate_sequences: {sequences}")
        if until_zero and all(x == 0 for x in sequences[-1]):
            break
        elif not until_zero and len(set(sequences[-1])) == 1:
            break
    return sequences


def part2(data):
    histories = parse_input(data)
    acc = 0  # Accumulator
    for history in histories:
        sequences = generate_sequences(history, until_zero=True)
        a = 0
        # Subtract current from the first value of the above sequence
        for sequence in sequences[::-1][1:]:
            a = sequence[0] - a
        acc += a
    return acc


tdata1 = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

if __name__ == "__main__":
    part1_answer = part1(tdata1)
    debug(f"Test 1: {part1_answer}")
    assert part1_answer == 114, "The expected output should be 114"

    part2_answer = part2(tdata1)
    debug(f"Test 2: {part2_answer}")
    assert part2_answer == 2, "The expected output should be 2"

    data = read_input_data(INPUT_FILE)
    start_p1 = time.perf_counter()
    part1_answer = part1(data)
    debug(f"Part 1 answer: {part1_answer}")
    debug(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")
    # # puzzle.answer_a = part1_answer

    start_p2 = time.perf_counter()
    part2_answer = part2(data)
    debug(f"Part 2 answer: {part2_answer}")
    debug(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
    # puzzle.answer_b = part2_answer
