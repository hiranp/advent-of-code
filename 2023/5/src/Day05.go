
package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "strings"
)

func main() {
    data, err := ioutil.ReadFile("input.txt")
    if err != nil {
        log.Fatal(err)
    }

    input := strings.Split(string(data), "\n")

    fmt.Println(part1(input))
    fmt.Println(part2(input))
}

func() part1(input []string) int {
    return 0
}

func() part2(input []string) int {
    return 0
}
