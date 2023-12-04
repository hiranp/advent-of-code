package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var wordToNum = map[string]int{
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

var td1 = "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"
var td2 = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`

func main() {
	data := readData("../input.txt")
	lines := strings.Split(string(data), "\n")

	// use td1 or td2 for testing
	// lines := strings.Split(td1, "\n")
	// lines = strings.Split(td2, "\n")

	part1Answer := part1(lines)
	fmt.Println("Part 1 answer:", part1Answer)

	part2Answer := part2(lines)
	fmt.Println("Part 2 answer:", part2Answer)
}

func readData(path string) string {
	data, err := os.ReadFile(path)
	if err != nil {
		fmt.Println("An error occurred.")
		fmt.Println(err)
		return ""
	}
	return string(data)
}

func part1(input []string) int {
	total := 0
	for _, line := range input {
		digits := []rune{}
		for _, ch := range line {
			if ch >= '0' && ch <= '9' {
				digits = append(digits, ch)
			}
		}
		if len(digits) > 0 {
			firstDigit := digits[0]
			lastDigit := digits[len(digits)-1]
			// println("firstDigit:", string(firstDigit))
			// println("lastDigit:", string(lastDigit))
			num, _ := strconv.Atoi(string([]rune{firstDigit, lastDigit}))
			total += num
		}
	}
	return total
}

func checkDigits(input string) string {
	if val, ok := wordToNum[input]; ok {
		return strconv.Itoa(val)
	}
	return input
}

// challenge no postive lookbehind in golang regex
// https://stackoverflow.com/questions/2973436/regex-look-behind-without-obvious-maximum-length-in-golang
func part2(lines []string) int {
	total := 0
	for _, line := range lines {
		digits := []string{}
		i := 0
		for i < len(line) {
			found := false
			for _, digit := range append(keys(wordToNum), "0", "1", "2", "3", "4", "5", "6", "7", "8", "9") {
				if strings.HasPrefix(line[i:], digit) {
					if _, ok := wordToNum[digit]; ok {
						digits = append(digits, checkDigits(digit))
					} else {
						digits = append(digits, digit)
					}
					i += len(digit)
					found = true
					break
				}
			}
			if !found {
				i++
			}
		}
		if len(digits) > 0 {
			println("line:", line)
			firstDigit := digits[0]
			lastDigit := digits[len(digits)-1]
			println("firstDigit:", firstDigit)
			println("lastDigit:", lastDigit)
			num, _ := strconv.Atoi(firstDigit + lastDigit)
			total += num
		}
	}
	return total
}

func keys(m map[string]int) []string {
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	return keys
}

func part22(lines []string) int {
	total := 0
	splitter := strings.Join(append(keys(wordToNum), "\\d"), "|")
	re := regexp.MustCompile(splitter)
	for _, line := range lines {
		for word, num := range wordToNum {
			line = strings.Replace(line, word, strconv.Itoa(num), -1)
		}
		println("line:", line)
		// matches := re.FindAllString(line, -1)
		digits := []string{}
		// for _, match := range matches {
		// 	digits = append(digits, match)
		// }
		digits = append(digits, re.FindAllString(line, -1)...)
		if len(digits) > 0 {
			firstDigit := digits[0]
			lastDigit := digits[len(digits)-1]
			if len(digits) == 1 {
				num, _ := strconv.Atoi(firstDigit)
				total += num
			} else {
				num, _ := strconv.Atoi(firstDigit + lastDigit)
				total += num
			}
		}
	}
	return total
}
