# Poker Hand
# https://open.kattis.com/problems/pokerhand
# TAGS: basic, dict
# CP4: 1.4h, Easy
# NOTES:
from collections import Counter

xs = input().split()

c = Counter(x[0] for x in xs)

print(max(c.values()))