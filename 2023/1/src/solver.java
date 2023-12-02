
// Creator: Hiran Patel
// Date: 2021-09-01
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.regex.*;

public class solver {
  static Map<String, Integer> wordToNum = new HashMap<String, Integer>() {
    {
      put("one", 1);
      put("two", 2);
      put("three", 3);
      put("four", 4);
      put("five", 5);
      put("six", 6);
      put("seven", 7);
      put("eight", 8);
      put("nine", 9);
    }
  };

  static String testData = "1abc2\n" + //
      "pqr3stu8vwx\n" + //
      "a1b2c3d4e5f\n" + //
      "treb7uchet";

  public static void main(String[] args) {
    // https://adventofcode.com/2023/day/1/input
    String data = readData("2023/1/input.txt");
    data = testData;
    String[] lines = data.split("\n");

    int part1Answer = part1(lines);
    System.out.println("Part 1 answer: " + part1Answer);

    int part2Answer = part2(lines);
    System.out.println("Part 2 answer: " + part2Answer);
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
   * 1. Find all digits in the string
   * 2. Add the first and last digits. If there is only one digit, add it twice
   * 3. Repeat for all lines
   * 
   * @param input
   * @return
   */
  public static int part1(String[] input) {
    int total = 0;
    for (String line : input) {
      List<Character> digits = new ArrayList<>();
      for (char ch : line.toCharArray()) {
        if (Character.isDigit(ch)) {
          digits.add(ch);
        }
      }
      if (!digits.isEmpty()) {
        char firstDigit = digits.get(0);
        char lastDigit = digits.size() > 1 ? digits.get(digits.size() - 1) : firstDigit;
        total += Integer.parseInt("" + firstDigit + lastDigit);
      }
    }
    return total;
  }

  public static String checkDigits(String input) {
    return wordToNum.containsKey(input) ? String.valueOf(wordToNum.get(input)) : input;
  }

  /**
   * Part 2
   * 1. Find all digits in the string. Convert words to digits
   * 2. Add the first and last digits. If there is only one digit, add it twice
   * 3. Repeat for all lines
   * 
   * @param input
   * @return
   */
  public static int part2(String[] lines) {
    int total = 0;
    String splitter = "(?=(" + String.join("|", wordToNum.keySet()) + "|\\d))";
    Pattern pattern = Pattern.compile(splitter);
    for (String line : lines) {
      Matcher matcher = pattern.matcher(line);
      List<String> digits = new ArrayList<>();
      while (matcher.find()) {
        digits.add(checkDigits(matcher.group()));
      }
      if (!digits.isEmpty()) {
        String firstDigit = digits.get(0);
        String lastDigit = digits.size() > 1 ? digits.get(digits.size() - 1) : firstDigit;
        total += Integer.parseInt(firstDigit + lastDigit);
      }
    }
    return total;
  }
}