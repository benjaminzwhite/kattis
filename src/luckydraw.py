# Lucky Draw
# https://open.kattis.com/problems/luckydraw
# TAGS: mathematics, probability, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
Nice probability exercise: I wrote detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/luckydraw.md
"""
from math import comb

# determined experimentally such that res does not change to within 1e-6 with the given testcases
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
    lose_this_round = comb(r - 1, k - 1) * (1 - p)**k * p**(r - k)

    # "a single player gets knocked out this round r, with all n-1 players having already been knocked out"
    res += lose_this_round * lose_before_this_round**(n - 1)

    lose_before_this_round += lose_this_round

# Note: the exercise wants the casino WIN probability
# This is just 1 - sum of the individual probabilities of each of the n players winning
# Since these individual probabilities - calculated above as res - are independent, the
# sum is just res + res + res ... n times, i.e. n * res:
print(1 - n * res)