# Square Peg in a Round Hole
# https://open.kattis.com/problems/squarepegs
# TAGS: greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
"""
The input plots is NOT SORTED despite the test case showing example where it is
"""
from math import sqrt

N, M, K = map(int, input().split())

plots = sorted(map(int, input().split()))

R = list(map(int, input().split()))
tmp = list(map(int, input().split()))
S = [x * sqrt(2) / 2 for x in tmp]

houses = sorted(R + S)

ip, ih = 0, 0
res = 0

while ip < len(plots) and ih < len(houses):
    if houses[ih] < plots[ip]:
        ih += 1
        res += 1
    ip += 1
    
print(res)