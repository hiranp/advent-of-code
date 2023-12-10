import java.io.File
import java.lang.Integer.max
import kotlin.math.lcm


// NOTE: This solution is not complete. It is a work in progress.
// Similiar to https://adventofcode.com/2019/day/20 Donut Maze
fun Int.println() = println(this)

data class Node(val left: String, val right: String)

fun parseInput(inputString: String): Pair<Map<String, Node>, String> {
    val lines = inputString.trim().split("\n")
    val nodes = mutableMapOf<String, Node>()
    for (line in lines.drop(2)) {  // Skip the first two lines
        if (" = " in line && ", " in line) {
            val (name, rest) = line.trim().split(" = ")
            val (left, right) = rest.trim('(', ')').split(", ")
            nodes[name] = Node(left, right)
        }
    }
    return nodes to lines[0]
}

/**
    * Navigate to the end of the path, and return the number of steps required.
    * @param currentNode The node to start from 
    * @param instructions The instructions to follow
    * @param nodes The map of nodes
    * @return The number of steps required to reach the end of the path
    */
**/
fun navigate1(currentNode: String, instructions: String, nodes: Map<String, Node>): Int {
    var steps = 0
    var currentNodeVar = currentNode
    for (instruction in generateSequence { instructions[steps % instructions.length] }) {
        currentNodeVar = if (instruction == 'L') nodes[currentNodeVar]?.left else nodes[currentNodeVar]?.right
        println("Node: $currentNodeVar, step $steps")
        steps++
        if (currentNodeVar == "ZZZ") {
            return steps
        }
    }
    return steps
}

/**
    * Navigate to the end of the path, and return the number of steps required.
    * @param currentNode The node to start from 
    * @param instructions The instructions to follow
    * @param nodes The map of nodes
    * @return The number of steps required to reach the end of the path
    */
**/
fun navigate2(currentNode: String, instructions: String, nodes: Map<String, Node>): Int {
    var sum = 0
    var currentNodeVar = currentNode
    while (!currentNodeVar.endsWith("Z")) {
        val i = instructions[sum % instructions.length]
        val n = nodes[currentNodeVar]
        currentNodeVar = if (i == 'L') n?.left else n?.right
        println("Node: $currentNodeVar")
        sum++
    }
    return sum
}


// --- Part One ---
// The first part of the problem is to find the number of steps required for a single node
// o reach the node ending with 'Z'. Basically a Camel Navigation Puzzle or Parking Functions.
fun part1(data: String): Int {
    val (nodes, instructions) = parseInput(data)
    return navigate1("AAA", instructions, nodes)
}

// --- Part Two ---
// To solve the second part of the problem, you need to modify the navigate function to
// handle multiple current nodes at once and continue until all current nodes end with 'Z'.
// You can use a set to keep track of the current nodes and update this set at each step
// based on the instructions.
fun part2(data: String): Int {
    val (nodes, instructions) = parseInput(data)
    val startNodes = nodes.keys.filter { it.endsWith("A") }
    val stepsFor = startNodes.map { navigate2(it, instructions, nodes) }
    return stepsFor.reduce { acc, i -> lcm(acc, i) }
}

fun readInput(filename: String): String {
    return File(filename).readText()
}

fun assertError(got: Int, want: Int) {
    if (got != want) {
        throw AssertionError("Error: got $got, want $want")
    }
}

fun main() {
    val test_data1 = """
        LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)
""".trimIndent()

    val test_data2 = """
        LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)
""".trimIndent()

    // test if implementation meets criteria from the description, like:
    val part1Answer = part1(test_data1)
    println("Steps required to reach ZZZ: $part1Answer")
    println("Test 1: $part1Answer")
    assertError(part1Answer, 6)

    val part2Answer = part2(test_data2)
    println("Test 2: $part2Answer")
    assertError(part2Answer, 6)

    // test if implementation meets criteria from the description, like:
    val data = readInput("../input.txt")
    val testAnswer1 = part1(data)
    println("Test 1: $testAnswer")
    val testAnswer2 = part2(data)
    println("Test 2: $testAnswer")

}
