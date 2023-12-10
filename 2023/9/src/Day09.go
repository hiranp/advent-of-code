package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

//TODO: Fix part 1, it's not working for some reason

// Debugging
var debugMode = false

func debug(args ...interface{}) {
	if debugMode {
		fmt.Println(args...)
	}
}

func readInputData(inputFile string) string {
	wd, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}
	fullPath := filepath.Join(wd, inputFile)
	data, err := os.ReadFile(fullPath)
	if err != nil {
		log.Fatalf("Failed to read file from path: %s, error: %v", fullPath, err)
	}
	return string(data)
}

func assertError(got, want int) {
	if got != want {
		fmt.Printf("Error: got %d, want %d\n", got, want)
	} else {
		fmt.Println("OK: ", got)
	}
}

func parseInput(inputData string) [][]int {
	lines := strings.Split(inputData, "\n")
	var data [][]int
	for _, line := range lines {
		if line != "" {
			nums := strings.Split(line, " ")
			var row []int
			for _, num := range nums {
				n, _ := strconv.Atoi(num)
				row = append(row, n)
			}
			data = append(data, row)
		}
	}
	return data
}

func generateSequences(history []int, untilZero bool) [][]int {
	sequences := [][]int{history}
	for {
		lastSeq := sequences[len(sequences)-1]
		var newSeq []int
		for i := 1; i < len(lastSeq); i++ {
			newSeq = append(newSeq, lastSeq[i]-lastSeq[i-1])
		}
		sequences = append(sequences, newSeq)
		if untilZero && allZero(newSeq) {
			break
		} else if !untilZero && allSame(newSeq) {
			break
		}
	}
	return sequences
}

func allZero(nums []int) bool {
	for _, num := range nums {
		if num != 0 {
			return false
		}
	}
	return true
}

func allSame(nums []int) bool {
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[0] {
			return false
		}
	}
	return true
}

func part1(data string) int {
	histories := parseInput(data)
	sum := 0
	for _, history := range histories {
		sequences := generateSequences(history, true)
		extrapolatedValue := history[len(history)-1] + sequences[len(sequences)-1][0]
		sum += extrapolatedValue
	}
	return sum
}

func part2(data string) int {
	histories := parseInput(data)
	acc := 0
	for _, history := range histories {
		sequences := generateSequences(history, true)
		a := 0
		for i := len(sequences) - 2; i >= 0; i-- {
			a = sequences[i][0] - a
		}
		acc += a
	}
	return acc
}

func main() {
	tdata1 := `
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
`
	part1Answer := part1(tdata1)
	debug("Test 1:", part1Answer)
	assertError(part1Answer, 114)

	part2Answer := part2(tdata1)
	debug("Test 2:", part2Answer)
	assertError(part2Answer, 2)

	data := readInputData("2023/9/input.txt")
	part1Answer = part1(data)
	debug("Part 1 answer:", part1Answer)

	part2Answer = part2(data)
	debug("Part 2 answer:", part2Answer)
}
