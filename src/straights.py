# Straights
# https://open.kattis.com/problems/straights
# TAGS: array, improve
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
"""
TODO: IMPROVE: maybe there is a better way
Couldn't think of a clever approach on attempt so just simulated it essentially:
-> move through the keys and remove straights and update the Counter info each loop
"""
from collections import Counter

N = int(input())
xs = map(int, input().split())

c = Counter(xs)

res = 0
while True:
    ks = sorted(c.keys())
    if not ks:
        break
    tmp = []
    for kl, kr in zip(ks, ks[1:] + [ks[0]]): # append ks[0] to end of 2nd zip so that wraparound triggers processing of current streak when reach the end of ks[1:]
        tmp.append(kl)
        if kr != kl + 1:
            res += 1
            for k in tmp:
                c[k] -= 1
                if c[k] == 0:
                    del c[k]
            tmp = []

print(res)