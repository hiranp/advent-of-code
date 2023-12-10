package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"strings"
)

const (
	INPUT_FILE = "../input.txt"
)

//TODO: Fix divide by zero error in part 2

// Read large input data from file, or use provided string as input data
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

// For small inputs, it's easier to just pass a string value
func getAllLines(fileName string) []string {

	// if file doesn't exist, try to treat as a string value. check if it contains newlines
	if _, err := os.Stat(path.Join("../", fileName)); os.IsNotExist(err) {
		if strings.Contains(fileName, "\n") {
			return strings.Split(fileName, "\n")
		}
	}

	bytes, _ := os.ReadFile(path.Join("../", fileName))

	return strings.Split(string(bytes), "\n")
}

func assertError(got, want int) {
	if got != want {
		fmt.Printf("Error: got %d, want %d\n", got, want)
	}
}

type Node struct {
	left  string
	right string
}

func parseInput(lines []string) (map[string]Node, string) {
	// lines := strings.Split(strings.TrimSpace(inputString), "\n")
	nodes := make(map[string]Node)
	for _, line := range lines[2:] { // Skip the first two lines
		if strings.Contains(line, " = ") && strings.Contains(line, ", ") {
			parts := strings.Split(strings.TrimSpace(line), " = ")
			name := parts[0]
			rest := strings.Trim(parts[1], "()")
			leftRight := strings.Split(rest, ", ")
			nodes[name] = Node{left: leftRight[0], right: leftRight[1]}
		}
	}
	return nodes, lines[0]
}

func navigate1(currentNode string, instructions string, nodes map[string]Node) int {
	steps := 0
	if len(instructions) == 0 {
		fmt.Println("Error: instructions string is empty")
		return 0
	}
	instructionsLen := len(instructions)
	for {
		instruction := instructions[steps%instructionsLen]
		if instruction == 'L' {
			currentNode = nodes[currentNode].left
		} else {
			currentNode = nodes[currentNode].right
		}
		fmt.Printf("Node: %s, step %d\n", currentNode, steps)
		steps++
		if currentNode == "ZZZ" {
			return steps
		}
	}
}

func navigate2(currentNode string, instructions string, nodes map[string]Node) int {
	sum := 0
	if len(instructions) == 0 {
		fmt.Println("Error: instructions string is empty")
		return 0
	}
	for !strings.HasSuffix(currentNode, "Z") {
		i := instructions[sum%len(instructions)]
		n := nodes[currentNode]
		if i == 'L' {
			currentNode = n.left
		} else {
			currentNode = n.right
		}
		fmt.Printf("Node: %s\n", currentNode)
		sum++
	}
	return sum
}

func part1(data []string) int {
	nodes, instructions := parseInput(data)
	steps := navigate1("AAA", instructions, nodes)
	return steps
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a, b int) int {
	return a / gcd(a, b) * b
}

func part2(data []string) int {
	nodes, instructions := parseInput(data)
	startNodes := []string{}
	for node := range nodes {
		if strings.HasSuffix(node, "A") {
			startNodes = append(startNodes, node)
		}
	}
	lcmSum := 1
	for _, node := range startNodes {
		steps := navigate2(node, instructions, nodes)
		lcmSum = lcm(lcmSum, steps)
	}
	return lcmSum
}

func main() {
	var data []string

	testData1 := `
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    `
	testData2 := `
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    `
	assertError(part1(readInputData(testData1)), 6)
	assertError(part2(readInputData(testData2)), 6)

	data = readInputData()
	fmt.Println(part1(data))
	fmt.Println(part2(data))
}
