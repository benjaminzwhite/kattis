# Smoothie Stand
# https://open.kattis.com/problems/smoothiestand
# TAGS: array, basic
# CP4: 3.2b, Iterative (Two Loops)
# NOTES:
k, r = map(int, input().split())

HAVE = list(map(int, input().split()))

res = 0

for _ in range(r):
    *NEED, price = map(int, input().split())
    qty = min(have // need for have, need in zip(HAVE, NEED) if need != 0)
    res = max(res, qty * price)

print(res)