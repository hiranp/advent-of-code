package src.solutions;

import src.meta.DayTemplate;

import java.util.*;

public class Day07 extends DayTemplate {

  /**
   * Main solving method.
   *
   * @param part1 The solver will solve part 1 if param is set to true.
   *              The solver will solve part 2 if param is set to false.
   * @param in    The solver will read data from this Scanner.
   * @return Returns answer in string format.
   */
  public String solve(boolean part1, Scanner in) {
    long answer = 0;
    List<Hand> hands = new ArrayList<>();
    while (in.hasNext()) {
      String line = in.nextLine();
      hands.add(new Hand(line.split(" ")[0], Integer.parseInt(line.split(" ")[1]), part1));
    }
    Collections.sort(hands);
    for (int i = 0; i < hands.size(); i++) {
      answer += hands.get(i).bid * (i + 1);
    }
    return answer + "";
  }
}

class Hand implements Comparable {
  int bid;
  int strength;
  int[] freqs = new int[13];
  int[] cards = new int[5];
  String[] ranks = new String[] { "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" };

  public Hand(String line, int bid, boolean part1) {
    if (!part1) {
      ranks = new String[] { "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J" };
    }
    this.bid = bid;
    int numJokers = 0;
    String[] s = line.split("");
    for (int i = 0; i < s.length; i++) {
      for (int j = 0; j < ranks.length; j++) {
        if (s[i].equals(ranks[j])) {
          if (!s[i].equals("J") || part1) {
            freqs[j]++;
          }
          if (s[i].equals("J") && !part1) {
            numJokers++;
          }
          cards[i] = j;
        }
      }
    }
    Arrays.sort(freqs);
    freqs[freqs.length - 1] += numJokers;
    strength = 2 * freqs[freqs.length - 1];
    if (freqs[freqs.length - 2] == 2) {
      strength += 1; // for full house and two pair
    }
  }

  @Override
  public int compareTo(Object o) {
    Hand other = (Hand) o;
    if (strength != other.strength) {
      return strength - other.strength;
    } else {
      for (int i = 0; i < cards.length; i++) {
        if (cards[i] != other.cards[i]) {
          return other.cards[i] - cards[i];
        }
      }
      return 0;
    }
  }
}