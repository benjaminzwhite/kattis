# Amalgamated Artichokes
# https://open.kattis.com/problems/artichoke
# TAGS: mathematics, basic
# CP4: 1.4f, Function
# NOTES:
from math import cos, sin

p, a, b, c, d, n = map(int, input().split())

def price(k):
    return p * (sin(a * k + b) + cos(c * k + d) + 2)

max_val = -float('inf')
res = 0

for k in range(1, n + 1):
    pr = price(k)
    max_val = max(max_val, pr)
    res = max(res, max_val - pr)

print(res)