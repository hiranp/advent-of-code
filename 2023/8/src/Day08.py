from aocd.models import Puzzle
import os
import time
import math
import itertools
from collections import namedtuple


# Constants
INPUT_FILE = "../input.txt"
Node = namedtuple("Node", ["left", "right"])


def get_input_data(input_file):
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
            data = file.read().split("\n")
        print(f"Using {input_file} for input data.")
    except FileNotFoundError:
        print(f"Input file {input_file} not found. Fetching data from AoC website.")
        puzzle = Puzzle(year=2023, day=8)
        data = puzzle.input_data.split("\n")
    return data


def parse_input(input_string):
    lines = input_string.strip().split("\n")
    nodes = {}
    for line in lines[2:]:  # Skip the first two lines
        if " = " in line and ", " in line:
            name, rest = line.strip().split(" = ")
            left, right = rest.strip("()").split(", ")
            nodes[name] = Node(left, right)
    return nodes, lines[0]


def navigate2(current_node, instructions, nodes):
    sum = 0
    while not current_node.endswith("Z"):
        i = instructions[sum % len(instructions)]
        n = nodes[current_node]
        if i == "L":
            current_node = n.left
        else:
            current_node = n.right
        print(f"Node: {current_node}")
        sum += 1
    return sum


def navigate1(current_node, instructions, nodes):
    steps = 0
    for instruction in itertools.cycle(instructions):
        if instruction == "L":
            current_node = nodes[current_node].left
        else:
            current_node = nodes[current_node].right
        print(f"Node: {current_node}, step {steps}")
        steps += 1
        if current_node == "ZZZ":
            return steps


# --- Part One ---
# The first part of the problem is to find the number of steps required for a single node
# to reach the node ending with 'Z'. Basically a Camel Navigation Puzzle or Parking Functions.
def part1(data):
    nodes, instructions = parse_input(data)
    steps = navigate1("AAA", instructions, nodes)
    return steps


# --- Part Two ---
# To solve the second part of the problem, you need to modify the navigate function to
# handle multiple current nodes at once and continue until all current nodes end with 'Z'.
# You can use a set to keep track of the current nodes and update this set at each step
# based on the instructions.
# """
def part2(data):
    nodes, instructions = parse_input(data)
    start_nodes = [node for node in nodes if node.endswith("A")]
    steps_for = [navigate2(node, instructions, nodes) for node in start_nodes]
    return math.lcm(*steps_for)


# if __name__ == "__main__":
#     test_data1 = """
#     LLR

#     AAA = (BBB, BBB)
#     BBB = (AAA, ZZZ)
#     ZZZ = (ZZZ, ZZZ)
#     """

#     nodes, instructions = parse_input(test_data1)
#     steps = navigate("AAA", instructions, nodes)
#     print(f"Steps required to reach ZZZ: {steps}")

#     # Read input.txt as a string
#     with open("2023/8/input.txt", "r") as file:
#         input_string = file.read()
#     nodes, instructions = parse_input(input_string)
#     steps = navigate("AAA", instructions, nodes)
#     print(f"Part1 Steps required to reach ZZZ: {steps}")


# def navigate2(current_nodes, instructions, nodes):
#     steps = 0
#     while not all(node.endswith("Z") for node in current_nodes):
#         next_nodes = set()
#         for node in current_nodes:
#             if instructions[steps % len(instructions)] == "L":
#                 next_nodes.add(nodes[node].left)
#                 print(f"Node: {node} Left: {nodes[node].left}")
#             else:
#                 next_nodes.add(nodes[node].right)
#                 print(f"Node: {node} Right: {nodes[node].right}")
#         current_nodes = next_nodes
#         steps += 1
#     return steps


# if __name__ == "__main__":
#     test_data1 = """
#     LR

#     11A = (11B, XXX)
#     11B = (XXX, 11Z)
#     11Z = (11B, XXX)
#     22A = (22B, XXX)
#     22B = (22C, 22C)
#     22C = (22Z, 22Z)
#     22Z = (22B, 22B)
#     XXX = (XXX, XXX)
#     """
#     # Read input.txt as a string
#     with open("2023/8/input.txt", "r") as file:
#         input_string = file.read()

#     nodes, instructions = parse_input(input_string)
#     start_nodes = {node for node in nodes if node.endswith("A")}
#     steps = navigate2(start_nodes, instructions, nodes)
#     print(f"P2 Steps required to reach ZZZ: {steps}")


if __name__ == "__main__":
    test_data1 = """
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    """

    test_data2 = """
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """

    print(test_data1)
    part1_answer = part1(test_data1)
    print(f"Steps required to reach ZZZ: {part1_answer}")
    print(f"Test 1: {part1_answer}")
    assert part1_answer == 6

    part2_answer = part2(test_data2)
    print(f"Test 2: {part2_answer}")
    assert part2_answer == 6

    # Read input.txt as a string
    with open("2023/8/input.txt", "r") as file:
        input_string = file.read()

    steps = part1(input_string)
    print(f"P1 Steps required to reach ZZZ: {steps}")
    steps = part2(input_string)
    print(f"P2 Steps required to reach ZZZ: {steps}")
    # data = read_input_data(INPUT_FILE)
    # start_p1 = time.perf_counter()
    # part1_answer = part1(data)
    # print(f"Part 1 answer: {part1_answer}")
    # # puzzle.answer_a = part1_answer
    # print(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")

    # start_p2 = time.perf_counter()
    # # part2_answer = part2(data)
    # # print(f"Part 2 answer: {part2_answer}")
    # # puzzle.answer_b = part2_answer
    # print(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
