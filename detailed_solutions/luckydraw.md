# Detailed solution for Kattis - Lucky Draw

[Problem statement on Kattis](https://open.kattis.com/problems/luckydraw)

A nice little probability exercise: looking at lengths of solutions on solution board it seems other people solved using dynamic programming (create a 2d dp array with states given by (r: generation, c: current lives)), and did not consider the following exact/analytical approach.

## Tags

probability

## Solution

- The inputs $`n`$ and $`k`$ correspond to $`n`$ players who all start with the **same** number of lives $`k`$.
- So all $`n`$ players are initially indistinguishable; therefore we can analyse any single player since they are all equally likely to be the Winner as defined below.
- A game ends with a win when there is a Winner. How is a Winner defined? We read: "when only one player remains"
- So a Winner is the last-man-standing, i.e. there must be a final round, $`R_{final}`$, where exactly 1 player has more than 0 lives and all other $`n - 1`$ players have 0 lives.
- This round $`R_{final}`$ can be any of the rounds from $`k`$ (since need at least $`k`$ rounds to knock out some players) to $`\infty`$ so we will consider these summation limits later.

### Probability calculation

In what follows, we call the current round $`r`$.

We are focusing on 1 single player, without loss of generality as discussed above.

Probability the player gets knocked out (i.e. loses the last of his $`k`$ lives) in current round $`r`$ having started the game with $`k`$ lives is given by:

1. choose $`k - 1`$ rounds to lose in, from $`r - 1`$ previous rounds, in $`\binom{r-1}{k-1}`$ ways
2. lose $`k - 1`$ times with probability: $`(1-p)^(k-1)`$
3. win  $`(r-1) - (k-1) = r-k`$ times with probability: $`p^(r-k)`$
4. then finally lose exactly 1 time (this round) with probability: $`(1-p)`$

This gives

$`\binom{r-1}{k-1} \times (1-p)^(k-1) \times p^(r-k) \times (1-p) = \binom{r-1}{k-1} (1-p)^k p^(r-k)`$ 

The probability the player is knocked out *before this current round r* is the sum of the above knockout probabilities, for each all rounds r' satisfying: k <= r' < r 
(where k <= r' i.e. lower limit is k rounds since any player need at least k rounds to lose k lives)

The probability that all n-1 other players are knocked out *before this current round r* is therefore the above summed probability multiplied (n-1) times since the games/outcomes for these n-1 other players are independent.

The total game result is the sum over paths i.e. for all possible number of game rounds. 
The upper limit is infinite: for programming implementation, we just take a MAX_ROUNDS such that the value is no longer changing within 1e-6 as per problem statement.
The lower limit is k itself since no game can last fewer than k rounds, as explained earlier.

## AC code

```python
from math import comb

# determined experimentally such that res does not change to within 10e-6 with the given testcases
MAX_ROUNDS = 1200

n, k, p = input().split()
n = int(n)
k = int(k)
p = float(p)

# store total SINGLE player win probability
res = 0

# total SINGLE player probability of losing at any round r' < r where r is current round
lose_before_this_round = 0 
for r in range(k, MAX_ROUNDS):
    lose_this_round = comb(r-1, k-1) * (1-p)**k * p**(r-k)

    # "a single player gets knocked out this round r, with all n-1 players having already been knocked out"
    res += lose_this_round * lose_before_this_round**(n-1)

    lose_before_this_round += lose_this_round

# note: the exercise wants the casino WIN probability
# This is just 1 - sum of (independent) probabilities of the n players winning
print(1 - res*n)
```
