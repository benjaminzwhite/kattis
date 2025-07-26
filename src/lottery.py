# Ticket Lottery
# https://open.kattis.com/problems/lottery
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
Judging by the difficulty rating/length of solutions on the leaderboard it seems people were solving
this with dynamic programming, but you can just solve it analytically as explained below O_o
"""
from math import comb

m, n, t, p = map(int, input().split())

all_states = comb(m, n)

total_good_states = 0

for num_our_winners in range(1, n + 1):
    # - choose the number of our winners in comb(p, num_our_winners) ways
    # - choose the (n - num_our_winners) other winners from "not-our-people", of which there are m - p, in comb(m - p, n - num_our_winners) ways
    # - finally, if these num_our_winners people can buy enough tickets for all of us, then we are good:
    if num_our_winners * t >= p:
        total_good_states += comb(p, num_our_winners) * comb(m - p, n - num_our_winners)

print(total_good_states / all_states)