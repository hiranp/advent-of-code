import java.io.File
import java.util.*

// This list will keep track of the number of scratchcards at each step
var cardCounts = mutableListOf<Int>()

fun getFile(filename: String): MutableList<String> {
    val inputs = mutableListOf<String>()
    val testFile = File("$filename")
    println("Reading file: ${testFile.absolutePath}")
    val scannerLines = Scanner(testFile)
    while (scannerLines.hasNextLine()) {
        inputs.add(scannerLines.nextLine())
    }
    scannerLines.close()
    return inputs
}

fun part1(data: List<String>): Int {
    var cardScore = 0
    var winNum = 0
    var theSum = 0
    val cardCounts = MutableList(data.size) { 1 }

    for ((x, row) in data.withIndex()) {
        val wins = row.split("|")[0].split(":")[1].trim().split(" ")
        val nums = row.split("|")[1].trim().split(" ")

        for (num in nums) {
            if (num in wins) {
                winNum++
                cardScore = if (cardScore == 0) 1 else cardScore * 2
            }
        }

        for (i in 0 until winNum) {
            if (x + i + 1 < cardCounts.size) {
                cardCounts[x + i + 1] += cardCounts[x]
            }
        }

        theSum += cardScore
        cardScore = 0
        winNum = 0
    }
    println("Card counts: $cardCounts")
    return theSum
}
fun part2(data: List<String>): Int {
    var cardScore = 0
    return cardScore
}


fun main() {
    // Test case
    // val data = mutableListOf<String>()
    val testData = getFile("../testdata1.txt")
    
    var testPoints = part1(testData)
    if (testPoints == 13) {
        println("Test passed!")
    } else {
        println("Test failed!")
        println("Expected: 13, Actual: $testPoints")
        System.exit(1)
    }

    val data = getFile("../input.txt")
    val totalPoints = part1(data)
    println("Total points: $totalPoints")
    val totalScratchCards = part2(data)
    println("Total points: $totalScratchCards")
}