# Jackpot
# https://open.kattis.com/problems/jackpot
# TAGS: logic, nice
# CP4: 5.3f, GCD and/or LCM
# NOTES:
"""
A bit overranked if you use a BigInt language (old exercise from 2003 I guess).

Also:
Weird output format where you output a string if res > 10**9.
CARE! I did not see that there is a '.' at the end of the required output string (not very small-laptop-screen friendly O_o)

Implementation note:
LCM not enabled in Python 3.8 so do DIY reduce GCD on xs with initially acc=1
"""
from math import gcd

n = int(input())
for _ in range(n):
    _ = input()
    xs = map(int, input().split())
    acc = 1
    for x in xs:
        acc *= x // gcd(acc, x)
    if acc <= 10**9:
        print(acc)
    else:
        print("More than a billion.") # CARE! there needs to be a . here O_o