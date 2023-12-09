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
            data = file.readlines()
        print(f"Using {input_file} for input data.")
    except FileNotFoundError:
        print(f"Input file {input_file} not found. Fetching data from AoC website.")
        puzzle = Puzzle(year=2023, day=6)
        # Split the input data into lines
        data = puzzle.input_data.split("\n")
    return data


def calculate_ways_to_win(lines):
    """
    1. For each race, calculate the maximum distance the boat can travel for each possible button hold time.
    2. Compare each maximum distance with the record distance for the race.
    3. Count the number of times the maximum distance is greater than the record distance.
    4. Multiply the counts for all races to get the final answer.
    """
    if len(lines) < 3:
        print("Error: Insufficient data. Please provide both time and distance data.")
        return

    times = lines[1].split(":")[1].strip().split()
    times = [int(t) for t in times]
    distances = lines[2].split(":")[1].strip().split()
    distances = [int(d) for d in distances]
    print(f"Times: {times}")
    print(f"Distances: {distances}")

    ways_to_win = 1
    for t, d in zip(times, distances):
        count = 0
        for i in range(t):
            max_distance = i * (t - i)
            if max_distance > d:
                count += 1
        ways_to_win *= count
    return ways_to_win


def calculate_ways_to_win_single_race(lines):
    """
    1. Calculate the maximum distance the boat can travel for each possible button hold time.
    2. Compare each maximum distance with the record distance for the race.
    3. Count the number of times the maximum distance is greater than the record distance.
    """
    # Split the test data into lines, assign the first line to times and the second line to distances
    times = lines[0].split(": ")[1].strip()
    print(f"Times: {times}")
    combined_times = int(times.replace(" ", ""))
    print(f"combined_times {combined_times}")
    distances = lines[1].split(": ")[1].strip()
    print(f"Distances: {distances}")
    combined_distances = int(distances.replace(" ", ""))  # Use int instead of long
    print(f"combined_distances {combined_distances}")

    count = 0
    for i in range(combined_times):  # Use combined_times instead of time
        max_distance = i * (combined_times - i)
        if max_distance > combined_distances:
            count += 1
    return count


def part2(data):
    pass


if __name__ == "__main__":
    test_data = """
Time:      7  15   30
Distance:  9  40  200
"""

    lines = test_data.split("\n")
    part1_answer = calculate_ways_to_win(lines)
    print(f"Test 1: {part1_answer}")
    assert part1_answer == 288

    # part2_answer = calculate_ways_to_win_single_race(lines)
    # print(f"Test 2: {part2_answer}")
    # assert part2_answer == 71503

    data = read_input_data(INPUT_FILE)
    print(f"Data: {data}")

    start_p1 = time.perf_counter()
    print(f"Part 1 answer: {calculate_ways_to_win(data)}")

    # # puzzle.answer_a = part1_answer
    print(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")

    start_p2 = time.perf_counter()
    print(f"Part 2 answer: {calculate_ways_to_win_single_race(data)}")

    # # puzzle.answer_b = part2_answer
    print(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
