# Dividing Sequence
# https://open.kattis.com/problems/sequence
# TAGS: binary, basic
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
Weird, kind of trick/troll question:

Based on the (4+ difficulty) and test case 6: 1 -> 3 -> 6 I thought it would be asking for building chain
of divisors such that all divide the next and the last one would be N itself etc.

But it's just asking for longest chain WITHOUT ANY restriction on N:
So just pack as many multiples of 2 as possible 1,2,4,8,...until <= N
"""
from math import log2, floor

n = int(input())

b = floor(log2(n)) + 1

print(b)

res = [1 << i for i in range(b)]

print(*res)