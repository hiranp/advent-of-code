package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var total int
var schematic []string
var gearNums = make(map[string][]int)

func main() {
	file, _ := os.Open("../input.txt")
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		schematic = append(schematic, scanner.Text())
	}

	fmt.Println("Part 1: ", part1())
	fmt.Println("Part 2: ", part2())
}

var numPattern = regexp.MustCompile(`\d+`)

func part1() int {

	for row := 0; row < len(schematic); row++ {
		matches := numPattern.FindAllStringIndex(schematic[row], -1)
		for _, match := range matches {
			num, _ := strconv.Atoi(schematic[row][match[0]:match[1]])
			if considerNumberNeighbors(row-1, match[0]-1, row+1, match[1], num) {
				total += num
			}
		}
	}
	return total
}

func part2() int {
	ratioTotal := 0
	for _, v := range gearNums {
		if len(v) == 2 {
			ratioTotal += v[0] * v[1]
		}
	}
	return ratioTotal
}

func considerNumberNeighbors(startY, startX, endY, endX, num int) bool {
	for y := startY; y <= endY; y++ {
		for x := startX; x <= endX; x++ {
			if y >= 0 && y < len(schematic) && x >= 0 && x < len(schematic[y]) {
				ch := schematic[y][x]
				if !strings.ContainsRune("0123456789.", rune(ch)) {
					if ch == '*' {
						key := fmt.Sprintf("%d,%d", y, x)
						gearNums[key] = append(gearNums[key], num)
					}
					return true
				}
			}
		}
	}
	return false
}
