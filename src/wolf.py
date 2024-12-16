# Wolf
# https://open.kattis.com/problems/wolf
# TAGS: logic, game, proof, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/wolf.md
"""
ME_CARDS = int(input())

d = {k:set() for k in "CDHS"}

for _ in range(ME_CARDS):
    val, suit = input().split()
    d[suit].add(int(val))

flg = False
for suit in "CDHS":
    if min(set(range(1, 14)).difference(d[suit]), default=float('inf')) < max(d[suit], default=0):
        flg = True

if ME_CARDS > 26 or (ME_CARDS == 26 and flg):
    print("possible")
else:
    print("impossible")