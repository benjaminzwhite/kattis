# Exits in Excess
# https://open.kattis.com/problems/exitsinexcess
# TAGS: graph, combinatorics, proof, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/exitsinexcess.md
"""
_, m = input().split()

blue, red = [], []

for i in range(1, int(m) + 1):
    u, v = map(int, input().split())
    if u < v:
        blue.append(i)
    else:
        red.append(i)

res = min((blue, red), key=len)

print(len(res))
for i in res:
    print(i)