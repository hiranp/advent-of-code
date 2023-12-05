package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// This slice will keep track of the number of scratchcards at each step
var cardCounts []int

func part1(data []string) int {
	// Initialize variables
	cardsScore, winNum, theSum := 0, 0, 0
	cardCounts = make([]int, len(data)+1) // Make sure the slice is large enough
	cardCounts[0] = 1                     // Initialize the first element to 1

	// For each row in the data
	for x, row := range data {
		// Split the row into winning numbers and your numbers
		parts := strings.Split(row, "|")
		wins := strings.Fields(parts[0][2:])
		nums := strings.Fields(parts[1])

		// For each of your numbers
		for _, num := range nums {
			// If the number is a winning number
			if contains(wins, num) {
				// Increment the number of winning numbers
				winNum++
				// Update the score for the card
				if cardsScore == 0 {
					cardsScore = 1
				} else {
					cardsScore *= 2
				}
			}
		}

		// Update the cardCounts slice based on the number of winning numbers
		for i := 0; i < winNum; i++ {
			cardCounts[x+i+1] += cardCounts[x]
		}

		// Add the score for the card to the total sum
		theSum += cardsScore

		// Reset the score and the number of winning numbers for the next card
		cardsScore, winNum = 0, 0
	}

	fmt.Printf("cardCounts: %v\n", cardCounts)
	return theSum
}

// TODO: This still not correct, we need to figure out how to calculate the total number of scratchcards
// getting incorrect answer of 15 instead of 30
func part2(data []string) int {
	// Calculate and return the total number of scratchcards
	return sum(cardCounts)
}

func sum(slice []int) int {
	total := 0
	for _, value := range slice {
		total += value
	}
	return total
}

func contains(arr []string, elem string) bool {
	for _, v := range arr {
		if v == elem {
			return true
		}
	}
	return false
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
			"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
			"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
			"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
			"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
			"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
			"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
			// Add more default data as needed
		}
	}

	// Calculate and print the total points from all the scratchcards
	part1Answer := part1(data)
	fmt.Printf("Part 1 answer: %d\n", part1Answer)

	// Calculate and print the total number of scratchcards
	part2Answer := part2(data)
	fmt.Printf("Part 2 answer: %d\n", part2Answer)
}
