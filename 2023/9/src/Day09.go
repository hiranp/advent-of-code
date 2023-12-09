package main

import (
	"bufio"
	"fmt"
	"os"
)

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

	// Read input data from file
	file, err := os.Open("../input2.txt")
	if err == nil {
		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			data = append(data, scanner.Text())
		}
		file.Close()
		fmt.Println("Using input.txt for input data.")
	} else {
		// Use default input data
		data = []string{
			"abc",
			// Add more default data as needed
		}
	}

	fmt.Println(part1(data))
	fmt.Println(part2(data))
}
