import java.awt.Point
import kotlin.math.max

val directions = listOf(Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1))
val pipeChars = "|-LJ7F"

fun isPipe(c: Char) = c in pipeChars

fun bfs(grid: List<String>, start: Point): Int {
    val queue = mutableListOf(start)
    val visited = mutableSetOf<Point>()
    val distance = mutableMapOf<Point, Int>()

    while (queue.isNotEmpty()) {
        val p = queue.removeAt(0)

        for (dir in directions) {
            val np = Point(p.x + dir.x, p.y + dir.y)

            if (np.x in grid.indices && np.y in grid[0].indices && isPipe(grid[np.x][np.y]) && np !in visited) {
                queue.add(np)
                visited.add(np)
                distance[np] = distance[p]!! + 1
            }
        }
    }

    return distance.values.maxOrNull() ?: 0
}

fun part1(input: List<String>): Int {
    val start = input.mapIndexed { i, row ->
        row.indexOf('S').takeIf { it != -1 }?.let { Point(i, it) }
    }.firstOrNull { it != null }!!

    return bfs(input, start)
}

fun main() {
    val input = listOf(
        "..F7.",
        ".FJ|.",
        "SJ.L7",
        "|F--J",
        "LJ..."
    )
    println(part1(input))
}