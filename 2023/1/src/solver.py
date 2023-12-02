from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=1)
data = puzzle.input_data
# print(data)

numbers = "one two three four five six seven eight nine".split()
word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def part1(input):
  total = 0
  # 1. Find first and last digit of each number
  # 2. Sum all numbers
  # 3. Return the sum

  for x in range(0, len(input)):
    digits = [ch for ch in input[x] if ch.isdigit()]
    # print(digits)
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
      print(f"Digits: {digits}")
      
      total += int(digits[0] + digits[-1])
  return total

lines = data.split("\n")
#lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

#lines = ["two1nine", "eight2three", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

# print(sum_numbers(lines))
# # Sum of all numbers in the puzzle input
# answer= sum(sum_numbers(lines))
# print(answer)

part1_answer = part1(lines)
print(f"Part 1 answer: {part1_answer}")

part2_answer = part2(lines)
print(f"Part 2 answer: {part2_answer}")

# puzzle.answer_a = part1_answer
puzzle.answer_b = part2_answer