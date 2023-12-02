import java.util.regex.*;
import java.util.*;
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

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
        // Current working directory
        String current_dir = System.getProperty("user.dir");
        Path relativePath = Paths.get(current_dir);
        File file = new File(relativePath.resolve(path).toString());
        Scanner scanner = new Scanner(file);
        StringBuilder data = new StringBuilder();
        while (scanner.hasNextLine()) {
            data.append(scanner.nextLine()).append("\n");
        }
        scanner.close();
        return data.toString();
    } catch (Exception e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
        return "";
    }
}

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
                    if ((color.equals("red") && count > 12) || (color.equals("green") && count > 13) || (color.equals("blue") && count > 14)) {
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