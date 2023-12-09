from aocd.models import Puzzle
import os
import time
from collections import Counter

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
        data = puzzle.input_data.split("\n")
    return data


def part1(data):
    """
    1. Define a dictionary to map card labels to their corresponding values.
    2. Define a function to calculate the strength of a hand. This function should return a tuple where the first element is the type of the hand and the second element is a list of card values sorted in descending order. The type of the hand can be determined by counting the occurrences of each card value in the hand.
    3. Read the input data and for each hand, calculate its strength and store it along with the bid amount.
    4. Sort the hands based on their strength.
    5. Calculate the total winnings by multiplying each hand's bid with its rank and summing up the results.
    """
    plays = []
    for line in data:
        parts = line.split()
        if len(parts) == 2:
            hand, bid = parts
            plays.append((hand, int(bid)))
            print(f"Hand: {hand}, Bid: {bid}")
    total = calculate_total(plays)
    return total


def part2(data):
    """
    1. Modify the classify function to treat J cards as wildcards.
        This means that if a hand contains a J card, we should consider all possible cards that the J card could
        represent and choose the one that gives the hand the highest classification.
    2. Modify the strength function to treat J cards as the weakest cards when sorting the cards in a hand.
        This means that if a hand contains a J card, it should be placed at the end of the sorted list of cards.
    """
    plays = []
    for line in data:
        parts = line.split()
        if len(parts) == 2:
            hand, bid = parts
            plays.append((hand, int(bid)))
    plays.sort(key=lambda play: strength_j(play[0]))
    print(f"Plays: {plays}")
    return sum(rank * bid for rank, (hand, bid) in enumerate(plays, 1))


letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}


def classify_j(hand):
    counts = list(Counter(hand).values())
    if "J" in hand:
        possible_counts = [counts.remove("J")] + [
            counts.append(card) for card in "AKQT98765432"
        ]
        return max(classify_counts(counts) for counts in possible_counts)
    else:
        return classify_counts(counts)


def classify_counts(counts):
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 2:
        return 2
    if 2 in counts:
        return 1
    return 0


def strength_j(hand):
    return (
        classify_j(hand),
        sorted(
            [letter_map.get(card, card) for card in hand if card != "J"]
            + ["J" for _ in range(hand.count("J"))],
            reverse=True,
        ),
    )


def classify(hand):
    # converts the dict_values object to a list, so you can use the count method on it.
    counts = list(Counter(hand).values())
    print(f"Counts: {counts}")
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 2:
        return 2
    if 2 in counts:
        return 1
    return 0


def strength(hand):
    return (
        classify(hand),
        sorted([letter_map.get(card, card) for card in hand], reverse=True),
    )


def calculate_total(plays):
    plays.sort(key=lambda play: strength(play[0]))
    return sum(rank * bid for rank, (hand, bid) in enumerate(plays, 1))


if __name__ == "__main__":
    tdata = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
    # Remove empty lines
    lines = [line for line in tdata.split("\n") if line.strip()]
    # print(lines)
    part1_tst = part1(lines)
    print(f"Test 1: {part1_tst}")
    assert part1_tst == 6440

    part2_tst = part2(lines)
    print(f"Test 2: {part2_tst}")

    # data = read_input_data(INPUT_FILE)
    # print(data)
    # start_p1 = time.perf_counter()
    # part1_answer = calculate_winnings(data)
    # print(f"Part 1 answer: {part1_answer}")
    # # puzzle.answer_a = part1_answer
    # print(f"Part 1 time: {time.perf_counter() - start_p1:.5f} Sec.")

    # start_p2 = time.perf_counter()
    # part2_answer = part2(data)
    # print(f"Part 2 answer: {part2_answer}")
    # puzzle.answer_b = part2_answer
    # print(f"Part 2 time: {time.perf_counter() - start_p2} Sec.")
