package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	INPUT_FILE = "../input.txt"
)

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

func part1(input []string) int {
	// TODO: Implement part1 logic here
	return 0
}

func part2(input []string) int {
	// TODO: Implement part2 logic here
	return 0
}

func main() {
	var data []string

	tdata := `
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
`
	assertError(part1(strings.Split(tdata, "\n")), 1)

	fmt.Println(part1(data))
	fmt.Println(part2(data))
}
