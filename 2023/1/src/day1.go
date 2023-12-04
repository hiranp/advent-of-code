package day1

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// Open the input file.
	file, err := os.Open("../input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close()

	// Create a scanner to read the file line by line.
	scanner := bufio.NewScanner(file)

	// Create a slice to store the calibration values.
	calibrationValues := []int{}

 // Read the file line by line and add the calibration values to the slice.
	for scanner.Scan() {
			text := scanner.Text()
			value, err := strconv.Atoi(text)
			if err != nil {
					// Try to convert word to number.
					value, err = wordToNumber(text)
					if err != nil {
							fmt.Println(err)
							os.Exit(1)
					}
			}
			calibrationValues = append(calibrationValues, value)
	}
	}

	// Calculate the sum of all the calibration values.
	sum := 0
	for _, value := range calibrationValues {
		sum += value
	}

	// Print the sum of all the calibration values.
	fmt.Println(sum)
}
