import java.io.File
import java.net.URL
import java.util.regex.Pattern

// Constants
val INPUT_FILE = "../input.txt"

fun readInputData(inputFile: String): List<String> {
    val cwd = File("").absolutePath
    val file = File("$cwd/$inputFile")
    return if (file.exists()) {
        println("Using $inputFile for input data.")
        file.readLines()
    } else {
        println("Input file $inputFile not found. Fetching data from AoC website.")
        // Exit
        emptyList<String>().also { System.exit(1) }
    }
}

  /**
   * Part 1
   * 1. Find all digits in the string
   * 2. Add the first and last digits. If there is only one digit, add it twice
   * 3. Repeat for all lines
   * 
   * @param input
   * @return sum of all digits
   */
fun part1(input: List<String>): Int {
    var total = 0
    for (x in input.indices) {
        val digits = input[x].filter { it.isDigit() }
        if (digits.isNotEmpty()) {
            total += (digits.first().toString() + digits.last().toString()).toInt()
        }
    }
    return total
}

  /**
   * Part 2
   * 1. Find all digits in the string. Convert words to digits
   * 2. Add the first and last digits. If there is only one digit, add it twice
   * 3. Repeat for all lines
   * 
   * @param lines
   * @return sum of all digits
   */
fun part2(lines: List<String>): Int {
    var total = 0
    val wordToNum = mapOf("one" to 1, "two" to 2, "three" to 3, "four" to 4, "five" to 5, "six" to 6, "seven" to 7, "eight" to 8, "nine" to 9)
    val sortedKeys = wordToNum.keys.sortedBy { it.length }
    val pattern = Regex(sortedKeys.joinToString("|") + "|\\d+")
    for (line in lines) {
        println("Line: $line")
        val words = mutableListOf<String>()
        var i = 0
        while (i < line.length) {
            val match = pattern.find(line.substring(i))
            if (match != null) {
                words.add(match.value)
                i += match.value.length
            } else {
                i += 1
            }
        }
        println("Words: $words")
        val number = words.map { word -> wordToNum[word]?.toString() ?: word }.joinToString("").toInt()
        val digits = number.toString().map { it.toString().toInt() }
        if (digits.isNotEmpty()) {
            println("Digits: $digits")
            val left = digits.first()
            val right = digits.last()
            println("Left: $left, Right: $right")
            total += (left + right).toInt()
            print("Total: $total")
        }
    }
    return total
}

fun alternative(lines: List<String>): Int {
    val wordToNum = mapOf("one" to 1, "two" to 2, "three" to 3, "four" to 4, "five" to 5, "six" to 6, "seven" to 7, "eight" to 8, "nine" to 9)
    var total = 0
    val splitter = "(?=(" + wordToNum.keys.joinToString("|") + "|\\d+))"
    val pattern = Regex(splitter)
    for (line in lines) {
        val matches = pattern.findAll(line)
        println("Line: $line")

        val digits = matches.mapNotNull { match -> 
            if (match.value.isNotEmpty()) {
                if (match.value.all { it.isDigit() }) {
                    match.value.toInt()
                } else {
                    wordToNum[match.value]
                }
            } else {
                null
            }
        }.toList()
        if (digits.isNotEmpty()) {
            println("Digits: $digits")
            val left = digits.first()
            val right = digits.last()
            println("Left: $left, Right: $right")
            total += (left + right).toInt()
        }
    }
    return total
}

fun main() {
    val test_data1 = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    """.trimIndent().split("\n")

    println("Test Data: $test_data1")
    val tdA = part1(test_data1)
    println("Test 1: $tdA")
    require(tdA == 142) { "Test 1 failed: $tdA is not equal to 142" }

    val test_data2 = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    """.trimIndent().split("\n")

    println("Test Data: $test_data2")
    val tdB = part2(test_data2)
    println("Test 2: $tdB")
    require(tdB == 281) { "Test 2 failed: $tdB is not equal to 281" }

    val input = readInputData(INPUT_FILE)
    val part1_answer = part1(input)
    println("Part 1: $part1_answer")
    val part2_answer = part2(input)
    println("Part 2: $part2_answer")

}
