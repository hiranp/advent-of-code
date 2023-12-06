from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=5)
data = puzzle.input_data
# print(data)


def part1(data):
    pass


def part2(data):
    pass


# part1_answer = part1(data)
# print(f"Part 1 answer: {part1_answer}")

# puzzle.answer_a = part1_answer

# part2_answer = part2(data)
# print(f"Part 2 answer: {part2_answer}")
# puzzle.answer_b = part2_answer


# def map_number(number, map):
#     for destination_start, source_start, length in map:
#         if source_start <= number < source_start + length:
#             return destination_start + (number - source_start)
#     return number


# def find_lowest_location(seeds, mappings):
#     locations = []
#     for seed in seeds:
#         soil = map_number(seed, mappings["seed-to-soil map"])
#         fertilizer = map_number(soil, mappings["soil-to-fertilizer map"])
#         water = map_number(fertilizer, mappings["fertilizer-to-water map"])
#         light = map_number(water, mappings["water-to-light map"])
#         temperature = map_number(light, mappings["light-to-temperature map"])
#         humidity = map_number(temperature, mappings["temperature-to-humidity map"])
#         location = map_number(humidity, mappings["humidity-to-location map"])
#         locations.append(location)
#     return min(locations)


# def parse_input(input):
#     mappings = {}
#     category = None
#     mapping = []
#     for line in input.split("\n"):
#         if line.endswith(":"):
#             if category:
#                 mappings[category] = mapping
#             category = line[:-1]
#             mapping = []
#         elif line:
#             if category == "seeds":
#                 mappings[category] = list(map(int, line.split()))
#             else:
#                 mapping.append(list(map(int, line.split())))
#     if category:
#         mappings[category] = mapping
#     return mappings


# sample_input = """
# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """


# mappings = parse_input(sample_input)
# print(find_lowest_location(mappings["seeds"], mappings))


# def map_number(number, map):
#     for destination_start, source_start, length in map:
#         if source_start <= number < source_start + length:
#             return destination_start + (number - source_start)
#     return number


# def find_lowest_location(
#     seeds,
#     seed_to_soil,
#     soil_to_fertilizer,
#     fertilizer_to_water,
#     water_to_light,
#     light_to_temperature,
#     temperature_to_humidity,
#     humidity_to_location,
# ):
#     locations = []
#     for seed in seeds:
#         soil = map_number(seed, seed_to_soil)
#         fertilizer = map_number(soil, soil_to_fertilizer)
#         water = map_number(fertilizer, fertilizer_to_water)
#         light = map_number(water, water_to_light)
#         temperature = map_number(light, light_to_temperature)
#         humidity = map_number(temperature, temperature_to_humidity)
#         location = map_number(humidity, humidity_to_location)
#         locations.append(location)
#     return min(locations)


def map_numbers(category_map, number):
    for dest_range_start, src_range_start, length in category_map:
        if src_range_start <= number < src_range_start + length:
            result = dest_range_start + (number - src_range_start)
            print(f"Mapped {number} to {result}")
            return result
    return number


def find_lowest_location(seeds, maps):
    categories = [
        "seed-to-soil map",
        "soil-to-fertilizer map",
        "fertilizer-to-water map",
        "water-to-light map",
        "light-to-temperature map",
        "temperature-to-humidity map",
        "humidity-to-location map",
    ]
    category_maps = {category: None for category in categories}

    # Parsing the input and organizing category maps
    current_category = None
    for line in maps:
        line = line.strip()
        if line in categories:
            current_category = line
            category_maps[current_category] = []
        elif current_category is not None and line:
            category_maps[current_category].append(tuple(map(int, line.split())))

    converted_locations = set()

    # Mapping the seeds to location
    for seed in seeds:
        soil = map_numbers(category_maps["seed-to-soil map"], seed)
        print(f"Seed: {seed}, Soil: {soil}")

        fertilizer = map_numbers(category_maps["soil-to-fertilizer map"], soil)
        print(f"Soil: {soil}, Fertilizer: {fertilizer}")

        water = map_numbers(category_maps["fertilizer-to-water map"], fertilizer)
        print(f"Fertilizer: {fertilizer}, Water: {water}")

        light = map_numbers(category_maps["water-to-light map"], water)
        print(f"Water: {water}, Light: {light}")

        temperature = map_numbers(category_maps["light-to-temperature map"], light)
        print(f"Light: {light}, Temperature: {temperature}")

        humidity = map_numbers(
            category_maps["temperature-to-humidity map"], temperature
        )
        print(f"Temperature: {temperature}, Humidity: {humidity}")

        location = map_numbers(category_maps["humidity-to-location map"], humidity)
        print(f"Humidity: {humidity}, Location: {location}")

        converted_locations.add(location)

    print(f"Converted Locations: {converted_locations}")  # Debug print

    if not converted_locations:  # If no locations were found
        return None

    return min(converted_locations)


if __name__ == "__main__":
    sample_input = """
    seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4
    """

    # Splitting the input by lines
    # lines = sample_input.split("\n")

    # def ints(s):
    #     return [int(m) for m in re.findall(r"-?[\d]+", s)]

    # parts = data.split("\n\n")
    # seed_names, map_sets = parts[0], parts[1:]
    # seeds = ints(parts[0])
    # min_location = 99999999999999999

    # for seed in seeds:
    #     location = seed
    #     for map_set in map_sets:
    #         for line in map_set.split("\n")[1:]:
    #             dst_start, src_start, rng = ints(line)
    #             if location in range(src_start, src_start + rng):
    #                 location = dst_start + (location - src_start)
    #                 break
    #     min_location = min(min_location, location)

    # print(f"Part 1: {min_location}")


import re

DAY_NUM = 5
DAY_DESC = "Day 5: If You Give A Seed A Fertilizer"


def calc(log, values, mode):
    seeds = list(map(int, values[0].split(": ")[1].split(" ")))
    all_maps = {}
    for row in values[2:] + [""]:
        m = re.search("([a-z]+)-to-([a-z]+) map:", row)
        if m is not None:
            source_type, dest_type = m.group(1), m.group(2)
            maps = []
        m = re.search("([0-9]+) ([0-9]+) ([0-9]+)", row)
        if m is not None:
            dest, source, count = int(m.group(1)), int(m.group(2)), int(m.group(3))
            maps.append((dest - source, source, source + count - 1))
        if len(row) == 0:
            all_maps[source_type] = {
                "target": dest_type,
                "maps": maps,
            }

    ret = None

    if mode == 1:
        seeds = [(x, x) for x in seeds]
    else:
        seeds = [
            (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
        ]

    pos = "seed"
    while pos in all_maps:
        next_seeds = []
        temp = all_maps[pos]
        pos = temp["target"]
        while len(seeds) > 0:
            a, b = seeds.pop(0)
            found = False
            for offset, c, d in temp["maps"]:
                if c <= a <= d and c <= b <= d:
                    next_seeds.append((a + offset, b + offset))
                    found = True
                    break
                elif c <= a <= d:
                    next_seeds.append((a + offset, d + offset))
                    seeds.append((d + 1, b))
                    found = True
                    break
                elif c <= b <= d:
                    seeds.append((a, c - 1))
                    next_seeds.append((c + offset, b + offset))
                    found = True
                    break
                elif a < c and b > d:
                    seeds.append((d + 1, b))
                    seeds.append((a, c - 1))
                    next_seeds.append((c + offset, d + offset))
                    found = True
                    break
            if not found:
                next_seeds.append((a, b))
        seeds = next_seeds

    ret = min(x[0] for x in seeds)
    return ret


def test(log):
    values = log.decode_values(
        """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
    """
    )

    log.test(calc(log, values, 1), "35")
    log.test(calc(log, values, 2), "46")


def run(log, values):
    log(calc(log, values, 1))
    log(calc(log, values, 2))


if __name__ == "__main__":
    import sys, os

    def find_input_file():
        for fn in sys.argv[1:] + ["../input.txt"]:
            for dn in [[], ["Puzzles"], ["..", "Puzzles"]]:
                cur = os.path.join(*(dn + [fn]))
                if os.path.isfile(cur):
                    return cur

    fn = find_input_file()
    if fn is None:
        print("Unable to find input file!\nSpecify filename on command line")
        exit(1)
    print(f"Using '{fn}' as input file:")
    with open(fn) as f:
        values = [x.strip("\r\n") for x in f.readlines()]
    print(f"Running day {DAY_DESC}:")
    run(print, values)
