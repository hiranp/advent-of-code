from aocd.models import Puzzle
import os

"""
This script solves the puzzle involving a set of scratchcards. Each scratchcard has two lists of numbers separated by '|':
    - A list of winning numbers
    - A list of numbers you have
The goal is to figure out which of the numbers you have appear in the list of winning numbers. 
The first match gives 1 point, and each subsequent match doubles the card's point value.
"""

# This list will keep track of the number of scratchcards at each step
cardcounts = []


def part1(data):
    """
    This function calculates the total points from all the scratchcards.
    """
    cardscore, winnum, thesum = 0, 0, 0

    # Initialize the cardcounts list with 1 for each card
    for _ in data:
        cardcounts.append(1)

    # For each row in the data
    for x, row in enumerate(data):
        # Split the row into winning numbers and your numbers
        wins = row.split("|")[0].split(":")[1].split()
        nums = row.split("|")[1].split()

        # For each of your numbers
        for num in nums:
            # If the number is a winning number
            if num in wins:
                # Increment the number of winning numbers
                winnum += 1
                # Update the score for the card
                if cardscore == 0:
                    cardscore = 1
                else:
                    cardscore *= 2

        # Update the cardcounts list based on the number of winning numbers
        for i in range(winnum):
            cardcounts[x + i + 1] += cardcounts[x]

        # Add the score for the card to the total sum
        thesum += cardscore

        # Reset the score and the number of winning numbers for the next card
        cardscore, winnum = 0, 0

    return thesum


def part2(data):
    """
    This function calculates the total number of scratchcards.
    """
    return sum(cardcounts)


if __name__ == "__main__":
    # If the input file is readable, use it instead of the default input data
    if os.access("../input.txt", os.R_OK):
        with open("../input.txt", "r") as file:
            data = file.read().split("\n")
        print("Using input.txt for input data.")
    else:
        # If the input file is not readable, use the default input data
        puzzle = Puzzle(year=2023, day=4)
        data = puzzle.input_data.split("\n")

    # Calculate and print the total points from all the scratchcards
    part1_answer = part1(data)
    print(f"Part 1 answer: {part1_answer}")
    # puzzle.answer_a = part1_answer

    # Calculate and print the total number of scratchcards
    part2_answer = part2(data)
    print(f"Part 2 answer: {part2_answer}")
    # puzzle.answer_b = part2_answer
