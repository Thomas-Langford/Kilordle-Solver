# Kilordle Solver
## Premise
Kilordle is a wordle-like game by jones and can be found [here](https://jonesnxt.github.io/kilordle/). It's exactly what it sound like, you play 1000 wordles at once. You're given 1005 guesses to do so. However, there is one difference between the kilordle and other wordle-likes such as the Octordle or Sedecordle. Kilordle will automatically solve a word for you if you've correctly placed each individual letter of a word in separate guesses. That way you don't need to do the trivial task of typing in a word where all letters have been solved. As a consequence, the minimum number of guesses required is much less than 1000. It can be solved by hand with well under 200 guesses. This repository aims to find the least number of guesses needed to solve any Kilordle.

## Theoretically Optimal Solution
Solving the Kilordle in as few guesses as possible boils down to finding the minimum number of words needed to place every letter in every position. If we pretend that any string of 5 characters would be accepted as a guess, then the optimal solution would be 30 guesses. This is because we could just group the letters into 5 5-letter groups (excluding z), and guess every cycle of each group. For example:<br>
abcde<br>
bcdea<br>
cdeab<br>
deabc<br>
eabcd<br>
This would be one such cycle. We could repeat this for the 4 other groups of 5 letters, resulting in 25 guesses, and adding the 5 guesses needed to place z in each position leaves us with a total of 30 guesses. Of course, abcde, bcdea, etc. are not words, so finding perfect cycles like this is impossible.

## Current Solution
The current solution is 36 guesses. It can be found [here](https://github.com/Thomas-Langford/Kilordle-Solver/blob/main/out.txt)