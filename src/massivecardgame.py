# Massive Card Game
# https://open.kattis.com/problems/massivecardgame
# TAGS: improve, binary search
# CP4: 3.3a, Binary Search
# NOTES:
"""
TODO: IMPROVE: Maybe can do better with a order statistics tree?
"""
from bisect import bisect_left, bisect_right

tmp = input()

xs = sorted(map(int, input().split()))

for _ in range(int(input())):
    l, r = map(int, input().split())
    res = bisect_right(xs, r) - bisect_left(xs, l)
    print(res)