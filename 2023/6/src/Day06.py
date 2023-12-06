import math
import time
import os

# Open the input file
cwd = os.getcwd()
with open(f"{cwd}/../input.txt", "r") as f:
    lines = f.readlines()

# Parse the times and distances from the input file
times = lines[0].split(": ")[1].strip().split()
times = [int(t) for t in times]
distances = lines[1].split(": ")[1].strip().split()
distances = [int(d) for d in distances]


def ways_to_win(time, record_distance):
    ways = 0
    for i in range(time):
        speed = i
        time_remaining = time - i
        distance = speed * time_remaining
        if distance > record_distance:
            ways += 1
    return ways


time_start = time.perf_counter()
total_ways = [ways_to_win(t, d) for t, d in zip(times, distances)]

print(f"Part 1: {math.prod(total_ways)}")
print(f"Part1 Time: {time.perf_counter() - time_start:.5f} Sec.")

time_start = time.perf_counter()
timer = int("".join([str(t) for t in times]))
distance = int("".join([str(d) for d in distances]))

print(f"Part 2: {ways_to_win(timer, distance)}")
print(f"Part2 Time: {time.perf_counter() - time_start:.5f} Sec.")
