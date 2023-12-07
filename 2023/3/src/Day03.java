import java.util.*;
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.regex.*;

public class Day03 {
  static int total = 0;
  static ArrayList<String> schematic = new ArrayList<>();
  static HashMap<String, ArrayList<Integer>> gearNums = new HashMap<>();

  public static void main(String[] args) throws FileNotFoundException {
    Scanner input = null;
    try {
      Path filePath = Paths.get("2023/3/input.txt");
      input = new Scanner(filePath);
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    while (input.hasNextLine()) {
      schematic.add(input.nextLine());
    }

    System.out.print("Part 1: ");
    System.out.println(part1(schematic));
    System.out.print("Part 2: ");
    System.out.println(part2(schematic));
  }

  static int part1(ArrayList<String> schematic) {

    Pattern numPattern = Pattern.compile("\\d+");

    for (int row = 0; row < schematic.size(); row++) {
      Matcher matcher = numPattern.matcher(schematic.get(row));
      while (matcher.find()) {
        int num = Integer.parseInt(matcher.group());
        if (considerNumberNeighbors(row - 1, matcher.start() - 1, row + 1, matcher.end(), num)) {
          total += num;
        }
      }
    }
    return total;

  }

  static int part2(ArrayList<String> schematic) {
    int ratioTotal = 0;
    for (ArrayList<Integer> v : gearNums.values()) {
      if (v.size() == 2) {
        ratioTotal += v.get(0) * v.get(1);
      }
    }
    return ratioTotal;
  }

  static boolean considerNumberNeighbors(int startY, int startX, int endY, int endX, int num) {
    for (int y = startY; y <= endY; y++) {
      for (int x = startX; x <= endX; x++) {
        if (y >= 0 && y < schematic.size() && x >= 0 && x < schematic.get(y).length()) {
          char ch = schematic.get(y).charAt(x);
          if (!Character.isDigit(ch) && ch != '.') {
            if (ch == '*') {
              String key = y + "," + x;
              gearNums.putIfAbsent(key, new ArrayList<>());
              gearNums.get(key).add(num);
            }
            return true;
          }
        }
      }
    }
    return false;
  }

}
