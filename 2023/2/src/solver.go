package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	data := readData("../input.txt")
	fmt.Println("Part 1:")
	fmt.Println(part1(data))
	fmt.Println("Part 2:")
	fmt.Println(part2(data))
}

func readData(path string) string {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		fmt.Println("An error occurred.")
		fmt.Println(err)
		return ""
	}
	return string(data)
}

// Part 1
//  1. Parse the input data to extract the game ID and the sets of cubes revealed in each game.
//  2. For each game, check if any set of cubes revealed in the game contains more cubes of a certain color than the bag can contain.
//     If such a set is found, the game is impossible and should be skipped.
//  3. If no such set is found, the game is possible and its ID should be added to the sum.
func part1(data string) int {
	gameRegex := regexp.MustCompile(`Game (\d+): (.+)`)
	matches := gameRegex.FindAllStringSubmatch(data, -1)
	total := 0
	for _, match := range matches {
		gameId, _ := strconv.Atoi(match[1])
		sets := strings.Split(match[2], "; ")
		possible := true
		for _, set := range sets {
			cubeRegex := regexp.MustCompile(`(\d+) (\w+)`)
			cubeMatches := cubeRegex.FindAllStringSubmatch(set, -1)
			for _, cubeMatch := range cubeMatches {
				count, _ := strconv.Atoi(cubeMatch[1])
				color := cubeMatch[2]
				if (color == "red" && count > 12) || (color == "green" && count > 13) || (color == "blue" && count > 14) {
					possible = false
					break
				}
			}
			if !possible {
				break
			}
		}
		if possible {
			total += gameId
		}
	}
	return total
}

// part2
// 1. Parse the input data to extract the game ID and the sets of cubes revealed
// in each game.
// 2. For each game, find the maximum number of cubes of each color revealed in
// any set.
// This will give us the minimum number of cubes of each color that must have
// been in the bag for the game to be possible.
// 3. Calculate the power of this minimum set of cubes by multiplying the
// numbers of red, green, and blue cubes together.
// 4. Add up the powers of the minimum sets of cubes for all games.
func part2(data string) int {
	gameRegex := regexp.MustCompile(`Game (\d+): (.+)`)
	matches := gameRegex.FindAllStringSubmatch(data, -1)
	totalPower := 0
	for _, match := range matches {
		sets := strings.Split(match[2], "; ")
		minCubes := map[string]int{"red": 0, "green": 0, "blue": 0}
		for _, set := range sets {
			cubeRegex := regexp.MustCompile(`(\d+) (\w+)`)
			cubeMatches := cubeRegex.FindAllStringSubmatch(set, -1)
			for _, cubeMatch := range cubeMatches {
				count, _ := strconv.Atoi(cubeMatch[1])
				color := cubeMatch[2]
				if count > minCubes[color] {
					minCubes[color] = count
				}
			}
		}
		power := minCubes["red"] * minCubes["green"] * minCubes["blue"]
		totalPower += power
	}
	return totalPower
}
