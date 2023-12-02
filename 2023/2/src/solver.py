from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=2)
data = puzzle.input_data
print(data)

def part1(data):
  """
  1. Parse the input data to extract the game ID and the sets of cubes revealed in each game.
  2. For each game, check if any set of cubes revealed in the game contains more cubes of a certain color than the bag can contain. 
      If such a set is found, the game is impossible and should be skipped.
  3. If no such set is found, the game is possible and its ID should be added to the sum.
 """
  games = re.findall(r'Game (\d+): (.+)', data)
  total = 0
  for game in games:
    game_id, sets = game
    sets = sets.split('; ')
    possible = True
    for set in sets:
      cubes = re.findall(r'(\d+) (\w+)', set)
      for count, color in cubes:
        if (color == 'red' and int(count) > 12) or (color == 'green' and int(count) > 13) or (color == 'blue' and int(count) > 14):
          possible = False
          break
      if not possible:
        break
    if possible:
      total += int(game_id)
  return total

print(part1(data))

part1_answer = part1(data)
print(f"Part 1 answer: {part1_answer}")

puzzle.answer_a = part1_answer

def part2(data):
  """
  1. Parse the input data to extract the game ID and the sets of cubes revealed in each game.
  2. For each game, find the maximum number of cubes of each color revealed in any set. 
      This will give us the minimum number of cubes of each color that must have been in the bag for the game to be possible.
  3. Calculate the power of this minimum set of cubes by multiplying the numbers of red, green, and blue cubes together.
  4. Add up the powers of the minimum sets of cubes for all games.
  """
  games = re.findall(r'Game (\d+): (.+)', data)
  total_power = 0
  for game in games:
    game_id, sets = game
    sets = sets.split('; ')
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for set in sets:
      cubes = re.findall(r'(\d+) (\w+)', set)
      for count, color in cubes:
        min_cubes[color] = max(min_cubes[color], int(count))
    power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
    total_power += power
  return total_power

print(part2(data))

part2_answer = part2(data)
print(f"Part 2 answer: {part2_answer}")

# puzzle.answer_b = part2_answer