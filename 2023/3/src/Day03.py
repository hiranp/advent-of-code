from aocd.models import Puzzle
import re
from collections import defaultdict

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
]  # Output: 4361


def sum_part_numbers(schematic):
    """ "
    This function takes a schematic and returns the sum of all the numbers
    that are adjacent to a symbol.
    TODO: This function is not complete. Only works for the test case.
    """
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

total = 0
schematic = []
gear_nums = defaultdict(list)


def consider_number_neighbors(start_y, start_x, end_y, end_x, num):
    """
    This function takes a number and the coordinates of its neighbors
    and returns True if the number is adjacent to a symbol.
    """
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if y >= 0 and y < len(schematic) and x >= 0 and x < len(schematic[y]):
                if schematic[y][x] not in "0123456789.":
                    if schematic[y][x] == "*":
                        gear_nums[(y, x)].append(num)
                    return True
    return False


def part1(schematic):
    """
    This function takes a schematic and returns the sum of all the numbers
    that are adjacent to a symbol.
    """
    global total
    num_pattern = re.compile("\d+")

    for row_num in range(len(schematic)):
        for match in re.finditer(num_pattern, schematic[row_num]):
            if consider_number_neighbors(
                row_num - 1,
                match.start() - 1,
                row_num + 1,
                match.end(),
                int(match.group(0)),
            ):
                total += int(match.group(0))
    return total


def part2(schematic):
    """
    This function calculates finds the gear ratio of every gear and add them all
    """
    rat_total = 0
    for v in gear_nums.values():
        if len(v) == 2:
            rat_total += v[0] * v[1]
    return rat_total


with open("../input.txt", "r") as file:
    schematic = [line.strip() for line in file]

print("Part 1: ", part1(schematic))
print("Part 2: ", part2(schematic))
