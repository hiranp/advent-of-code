import java.io.File
import java.util.*

fun getFile(filename: String): File {
    val testFile = File("$filename")
    println("Reading file: ${testFile.absolutePath}")
    return testFile
}

fun part1(lines: Scanner): Int {
    var totalPoints = 0

    while (lines.hasNextLine()) {
        val line = lines.nextLine()
        val parts = line.split("|")
        val winningNumbers = parts[0].trim().split(" ")
        val yourNumbers = parts[1].trim().split(" ")

        val winningSet = winningNumbers.toHashSet()
        val yourSet = yourNumbers.toHashSet()

        winningSet.retainAll(yourSet) // Intersection of the two sets

        val matches = winningSet.size
        val points = if (matches > 0) Math.pow(2.0, (matches - 1).toDouble()).toInt() else 0

        totalPoints += points
    }

    return totalPoints
}

fun main() {
    // Test case
    val testFile = getFile("testdata1.txt")
    val testScanner = Scanner(testFile)
    val testPoints = part1(testScanner)
    testScanner.close()
    if (testPoints == 13) {
        println("Test passed!")
    } else {
        println("Test failed!")
        println("Expected: 13, Actual: $testPoints")
        System.exit(1)
    }

    // Actual input
    val inputFile = getFile("input.txt")
    val scanner = Scanner(inputFile)
    val totalPoints = part1(scanner)
    scanner.close()
    println("Total points: $totalPoints")
}