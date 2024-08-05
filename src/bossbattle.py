# Boss Battle
# https://open.kattis.com/problems/bossbattle
# TAGS: logic, proof
# CP4: 1.4i, Still Easy
# NOTES:
"""
After each bomb explodes, you eliminate 3 locations but then boss can crawl back in to 2 of them (leftmost and rightmost)

So after each explosion you only 100% deny 3-2 = 1 location.

Since each step reduces # of locations by 1, and you also win when num-remaining <= 3, you need n-2 steps.
Handle case also when n=1,2,3 separately (only 1 bomb needed)
"""
n = int(input())

print(n - 2 if n > 3 else 1)