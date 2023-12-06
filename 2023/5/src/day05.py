import time, re


# Function to load the data from the file
def load_data(file):
    try:
        with open(file) as f:
            return f.read().split("\n\n")
    except FileNotFoundError:
        print(f"File {file} not found.")


# Function to change the seed based on the converters
def change_seed(seed, converters, low=1):
    # Iterate over each converter in the list of converters
    for converter in converters:
        # Iterate over the converter list in steps of 3
        for i in range(0, len(converter), 3):
            # Extract the destination, source, and range values from the converter list
            dest, source, rng = converter[i : i + 3]

            # Check if the seed is outside the valid range for this converter
            if seed < source or seed > (source + rng - 1):
                # If the seed is outside the range, skip to the next converter
                continue

            # Check if the low value is set to -1 (indicating it hasn't been updated yet)
            if low == -1:
                # If low is -1, update it to the source + range value
                low = source + rng

            # Update the seed value based on the source and destination values
            seed = seed - source + dest

            # Break out of the inner loop since we found a matching converter
            break

    # Return the updated seed value and the low value
    return seed, low


# Function to solve the puzzle
def part1_2(puzzle):
    numbers = [list(map(int, re.findall("\d+", part))) for part in puzzle]
    seeds, converters = numbers[0], numbers[1:]
    min_seed = min_location = float("inf")

    for seed in seeds:
        seed, _ = change_seed(seed, converters)
        min_seed = min(min_seed, seed)

    #  converts each range of seed numbers to a range of location numbers and finds the minimum location number.
    pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    for low, high in pairs:
        while low < high:
            seed = low
            seed, low = change_seed(seed, converters, low=-1)
            min_location = min(min_location, seed)

    return min_seed, min_location


# Main execution
time_start = time.perf_counter()
part1_answer, part2_answer = part1_2(load_data("2023/5/input.txt"))
print(f"Part 1: {part1_answer}")
print(f"Part 2: {part2_answer}")
print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
