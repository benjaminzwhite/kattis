# Mastering Mastermind
# https://open.kattis.com/problems/mastermind
# TAGS: array, dict
# CP4: 2.2b, 1D Array, Harder
# NOTES:
from collections import defaultdict

n, xs, ys = input().split()

r, s = 0, 0
dxs = defaultdict(int)
dys = defaultdict(int)

for x, y in zip(xs, ys):
    if x == y:
        r += 1
    else:
        dxs[x] += 1
        dys[y] += 1

for x, cnt_x in dxs.items():
    s += min(cnt_x, dys.get(x, 0))

print(r, s)