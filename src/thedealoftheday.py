# The Deal of the Day
# https://open.kattis.com/problems/thedealoftheday
# TAGS: mathematics, combinatorics, logic
# CP4: 8.7h, Mathematics+Other
# NOTES:
from math import prod
from itertools import combinations

xs = [x for x in map(int, input().split()) if x != 0]
k = int(input())

res = sum(prod(c) for c in combinations(xs, k))

print(res)