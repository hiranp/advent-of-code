
/**
1. Define a dictionary to map card labels to their corresponding values.
2. Define a function to calculate the strength of a hand. This function should return a tuple where the first element is the type of the hand and the second element is a list of card values sorted in descending order. The type of the hand can be determined by counting the occurrences of each card value in the hand.
3. Read the input data and for each hand, calculate its strength and store it along with the bid amount.
4. Sort the hands based on their strength.
5. Calculate the total winnings by multiplying each hand's bid with its rank and summing up the results.
 */
// fun main() {
//     fun part1(input: List<String>): Int {
//         return input.size
//     }

//     fun part2(input: List<String>): Int {
//         return input.size
//     }

//     // test if implementation meets criteria from the description, like:
//     val testInput = readInput("test")
//     check(part1(testInput) == 1)

//     val input = readInput("input")
//     part1(input).println()
//     part2(input).println()
// }

import java.io.File

fun main() {
    val lines = File("input.txt").readLines().filter { it.isNotEmpty() }

    // Pre-calculate hand types and scores for part 1
    val handTypes = listOf(
        listOf(1, 1, 1, 1, 1),
        listOf(1, 1, 1, 2),
        listOf(1, 2, 2),
        listOf(1, 1, 3),
        listOf(2, 3),
        listOf(1, 4),
        listOf(5)
    )
    val handScores = handTypes.withIndex().associate { it.index to it.value }

    // Map card labels to their values for both parts
    val cardValues = mapOf(
        "J" to listOf(11, 10),
        "2" to 2,
        "3" to 3,
        "4" to 4,
        "5" to 5,
        "6" to 6,
        "7" to 7,
        "8" to 8,
        "9" to 9,
        "T" to 10,
        "Q" to 12,
        "K" to 13,
        "A" to 14
    )


fun hand(cards: String): Pair<Int, List<Int>> {
    val cardCounts = cards.groupingBy { it }.eachCount()

    val ts = mutableListOf(handScores[cardCounts.values.sortedBy { it }] ?: 0)
    for ((otherValue, otherCount) in cardCounts) {
        if (otherValue == 'J') continue
        val otherCardCount = cardCounts.values.sum() - otherCount
        ts.add(handScores[listOf(otherCount, otherCardCount).sortedBy { it }] ?: 0)
    }

    return Pair(
        (ts.filterNotNull()).maxOrNull()!!,
        (cards.map { cardValues[it]!! }.first()).filterNotNull().sortedDescending()
    )
}

    for (part in 1..2) {
        val hands = lines.map { line: String -> hand(line.split(" ").first()) to line.split(" ").last().toInt() }
            .sortedWith(compareByDescending { it.first })

        val totalScore = hands.withIndex().sumOf { (i, hand) -> i * hand.second + hand.second }
        println("Part $part: $totalScore")
    }
} // End of main()