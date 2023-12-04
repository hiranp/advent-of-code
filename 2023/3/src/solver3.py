from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=3)
data = puzzle.input_data
print(data)


schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def part1(data):
    pass


def part2(data):
    pass


def sum_part_numbers(schematic):
    symbols = set(["*", "#", "+", "$"])
    total = 0
    rows = len(schematic)
    cols = len(schematic[0])

    for i in range(rows):
        j = 0
        while j < cols:
            if schematic[i][j].isdigit():
                # Extract the whole number
                match = re.match(r"\d+", schematic[i][j:])
                number = int(match.group()) if match else 0
                end = j + len(match.group()) if match else j + 1

                # Check the eight surrounding characters for the whole number
                found_symbol = False
                for k in range(j, end):
                    for dx, dy in [
                        (-1, -1),
                        (-1, 0),
                        (-1, 1),
                        (0, -1),
                        (0, 1),
                        (1, -1),
                        (1, 0),
                        (1, 1),
                    ]:
                        nx, ny = i + dx, k + dy
                        if (
                            0 <= nx < rows
                            and 0 <= ny < cols
                            and schematic[nx][ny] in symbols
                        ):
                            found_symbol = True
                            break
                    if found_symbol:
                        break

                if found_symbol:
                    total += number
                    j = end
                else:
                    j += 1
            else:
                j += 1

    return total


print(f"test:", sum_part_numbers(schematic))  # Output: 4361


# # Read the schematic from a file
# with open("./input.txt", "r") as file:
#     schematic = [line.strip() for line in file]

# print(sum_part_numbers(schematic))

import re
import parse
import math
from collections import defaultdict

# Initialize the total sum and the board
total = 0
board = []
# A dictionary to store the numbers adjacent to each gear
gear_nums = defaultdict(list)


# Function to check the neighbors of a number and add it to the gear_nums dictionary if it is adjacent to a gear
def consider_number_neighbors(start_y, start_x, end_y, end_x, num):
    global gear_nums
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if y >= 0 and y < len(board) and x >= 0 and x < len(board[y]):
                if board[y][x] not in "0123456789.":
                    if board[y][x] == "*":
                        gear_nums[(y, x)].append(num)
                    return True
    return False


# Regular expression pattern for a number
num_pattern = re.compile("\d+")

# Read the schematic from the input file
for line in open("input.txt").readlines():
    board.append(line.strip())

# Iterate over each row in the board
for row_num in range(len(board)):
    # Find all the numbers in the row
    for match in re.finditer(num_pattern, board[row_num]):
        # If the number is adjacent to a symbol, add it to the total sum
        if consider_number_neighbors(
            row_num - 1,
            match.start() - 1,
            row_num + 1,
            match.end(),
            int(match.group(0)),
        ):
            total += int(match.group(0))

# Print the total sum
print(total)

# Initialize the total product
rat_total = 0

# For each gear, if it is adjacent to exactly two numbers, multiply them and add to the total product
for k, v in gear_nums.items():
    if len(v) == 2:
        rat_total += v[0] * v[1]

# Print the total product
print(rat_total)

# part1_answer = sum_part_numbers(data)
# print(f"Part 1 answer: {part1_answer}")

# puzzle.answer_a = part1_answer

# part2_answer = part2(data)
# print(f"Part 2 answer: {part2_answer}")
# puzzle.answer_b = part2_answer
