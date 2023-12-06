package src;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class solver4 {

  public static File getFile(String filename) {
    File testFile = Paths.get("2023/4/" + filename).toFile();
    // Print the absolute path of the file
    System.out.printf("Reading file: %s%n", testFile.getAbsolutePath());
    return testFile;
  }

  public static void main(String[] args) throws IOException {
    // Test case
    File testFile = getFile("testdata1.txt");

    Scanner testScanner = new Scanner(testFile);
    int testPoints = part1(testScanner);
    testScanner.close();
    if (testPoints == 13) {
      System.out.println("Test passed!");
    } else {
      System.out.println("Test failed!");
      System.out.println("Expected: 13, Actual: " + testPoints);
      System.exit(1);
    }

    // Actual input
    File inputFile = getFile("input.txt");
    Scanner scanner = new Scanner(inputFile);
    int totalPoints = part1(scanner);
    scanner.close();
    System.out.println("Total points: " + totalPoints);
  }

  public static int part1(Scanner lines) {
    int totalPoints = 0;

    while (lines.hasNextLine()) {
      String line = lines.nextLine();
      String[] parts = line.split("\\|");
      String[] winningNumbers = parts[0].trim().split(" ");
      String[] yourNumbers = parts[1].trim().split(" ");

      Set<String> winningSet = new HashSet<>(Arrays.asList(winningNumbers));
      Set<String> yourSet = new HashSet<>(Arrays.asList(yourNumbers));

      winningSet.retainAll(yourSet); // Intersection of the two sets

      int matches = winningSet.size();
      int points = matches > 0 ? (int) Math.pow(2, matches - 1) : 0;

      totalPoints += points;
    }

    return totalPoints;
  }
}