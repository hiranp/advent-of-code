// Creator: Hiran Patel
// Date: 2021-09-01

import java.util.regex.*;
import java.util.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class solver {
    public static void main(String[] args) {
        String data = readData("2023/2/input.txt");
        System.out.println("Part 1:");
        System.out.println(part1(data));
        System.out.println("Part 2:");
        System.out.println(part2(data));
    }

    public static String readData(String path) {
        try {
            Path filePath = Paths.get(path);
            return Files.readString(filePath);
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return "";
        }
    }

    /**
     * Part 1
     * 1. Parse the input data to extract the game ID and the sets of cubes revealed
     * in each game.
     * 2. For each game, check if any set of cubes revealed in the game contains
     * more cubes of a certain color than the bag can contain.
     * If such a set is found, the game is impossible and should be skipped.
     * 3. If no such set is found, the game is possible and its ID should be added
     * to the sum.
     * 
     * @param data
     * @return
     */
    public static int part1(String data) {
        Pattern gamePattern = Pattern.compile("Game (\\d+): (.+)");
        Matcher gameMatcher = gamePattern.matcher(data);
        int total = 0;
        while (gameMatcher.find()) {
            int gameId = Integer.parseInt(gameMatcher.group(1));
            String[] sets = gameMatcher.group(2).split("; ");
            boolean possible = true;
            for (String set : sets) {
                Pattern cubePattern = Pattern.compile("(\\d+) (\\w+)");
                Matcher cubeMatcher = cubePattern.matcher(set);
                while (cubeMatcher.find()) {
                    int count = Integer.parseInt(cubeMatcher.group(1));
                    String color = cubeMatcher.group(2);
                    if ((color.equals("red") && count > 12) || (color.equals("green") && count > 13)
                            || (color.equals("blue") && count > 14)) {
                        possible = false;
                        break;
                    }
                }
                if (!possible) {
                    break;
                }
            }
            if (possible) {
                total += gameId;
            }
        }
        return total;
    }

    /**
     * Part 2
     * 1. Parse the input data to extract the game ID and the sets of cubes revealed
     * in each game.
     * 2. For each game, find the maximum number of cubes of each color revealed in
     * any set.
     * This will give us the minimum number of cubes of each color that must have
     * been in the bag for the game to be possible.
     * 3. Calculate the power of this minimum set of cubes by multiplying the
     * numbers of red, green, and blue cubes together.
     * 4. Add up the powers of the minimum sets of cubes for all games.
     * 
     * @param data
     * @return
     */
    public static int part2(String data) {
        Pattern gamePattern = Pattern.compile("Game (\\d+): (.+)");
        Matcher gameMatcher = gamePattern.matcher(data);
        int totalPower = 0;
        while (gameMatcher.find()) {
            String[] sets = gameMatcher.group(2).split("; ");
            Map<String, Integer> minCubes = new HashMap<>();
            minCubes.put("red", 0);
            minCubes.put("green", 0);
            minCubes.put("blue", 0);
            for (String set : sets) {
                Pattern cubePattern = Pattern.compile("(\\d+) (\\w+)");
                Matcher cubeMatcher = cubePattern.matcher(set);
                while (cubeMatcher.find()) {
                    int count = Integer.parseInt(cubeMatcher.group(1));
                    String color = cubeMatcher.group(2);
                    minCubes.put(color, Math.max(minCubes.get(color), count));
                }
            }
            int power = minCubes.get("red") * minCubes.get("green") * minCubes.get("blue");
            totalPower += power;
        }
        return totalPower;
    }

}