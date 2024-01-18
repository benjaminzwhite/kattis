# Ptice
# https://open.kattis.com/problems/ptice
# TAGS: array
# CP4: 1.4h, Easy
# NOTES:
from itertools import cycle

N = int(input())
s = input()

best = -1
winners = []

for name, pattern in zip(("Adrian", "Bruno", "Goran"), (cycle("ABC"), cycle("BABC"), cycle("CCAABB"))):
    res = sum(u == l for u, l in zip(pattern, s))
    if res > best:
        best = res
        winners = [name]
    elif res == best:
        winners.append(name)

print(best)
for name in winners:
    print(name)