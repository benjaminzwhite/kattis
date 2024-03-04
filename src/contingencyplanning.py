# Contingency Planning
# https://open.kattis.com/problems/contingencyplanning
# TAGS: basic, mathematics, combinatorics
# CP4: 3.2a, Pre-calculate-able
# NOTES:
"""
Reading comprehension - it asks towards the end "choose from 1 to n zombies, then permute the orders in which that subset arrives"

It asks to skip/ignore the {} subset, so either remove 1 from total count with i in range(0, n+1) or just
calculate the sum over range(1, n+1) instead.

Found experimentally that n >= 12 case is greater than 10**9.
"""
from math import comb, factorial

n = int(input())

# 10**9 exceeded for n >= 12:
if n >= 12:
    print("JUST RUN!!")
else:
    res = sum(comb(n, i) * factorial(i) for i in range(1, n + 1)) # at least 1 zombie so skip i=0 subset
    print(res)