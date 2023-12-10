package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	INPUT_FILE = "../input.txt"
)

type Play struct {
	hand string
	bid  int
}

func main() {
	tdata := `
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
`
	assertError(part1(strings.Split(tdata, "\n")), 1390)

	data := readInputData(INPUT_FILE)
	fmt.Println(part1(data))
	fmt.Println(part2(data))
}

func readInputData(args ...string) []string {
	var lines []string

	if len(args) > 0 {
		// Use the provided string as input data
		lines = strings.Split(args[0], "\n")
		fmt.Println("Using provided string for input data.")
	} else {
		// Read input lines from file
		file, err := os.Open(INPUT_FILE)
		if err == nil {
			scanner := bufio.NewScanner(file)
			for scanner.Scan() {
				lines = append(lines, scanner.Text())
			}
			file.Close()
			fmt.Println("Using input.txt for input data.")
		} else {
			// Handle error
			fmt.Println("Error opening file:", err)
		}
	}

	return lines
}

func assertError(got, want int) {
	if got != want {
		fmt.Printf("Error: got %d, want %d\n", got, want)
	}
}

func part1(data []string) int {
	var plays []Play
	for _, line := range data {
		parts := strings.Split(line, " ")
		if len(parts) == 2 {
			hand := parts[0]
			bid, _ := strconv.Atoi(parts[1])
			plays = append(plays, Play{hand, bid})
		}
	}
	sort.Slice(plays, func(i, j int) bool {
		return strength(plays[i].hand) < strength(plays[j].hand)
	})
	total := 0
	for i, play := range plays {
		total += (i + 1) * play.bid
	}
	return total
}
func part2(data []string) int {
	total := 0
	for _, hand := range data {
		total += strengthJ(hand)
	}
	return total
}

func strength(hand string) int {
	// This is a placeholder implementation.
	// Replace this with the actual logic to calculate the strength of a hand.
	score := 0
	for _, card := range hand {
		score += int(card)
	}
	return score
}

func strengthJ(hand string) int {
	// This is a placeholder implementation.
	// Replace this with the actual logic to calculate the strength of a hand.
	score := 0
	for _, card := range hand {
		score += int(card) * 2 // Assume that J cards count double
	}
	return score
}
