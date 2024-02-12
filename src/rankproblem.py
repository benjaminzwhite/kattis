# A Rank Problem
# https://open.kattis.com/problems/rankproblem
# TAGS: array
# CP4: 2.2a, 1D Array, Medium
# NOTES:
n, m = map(int, input().split())

xs = ['T' + str(x) for x in range(1, n + 1)]

for _ in range(m):
    twin, tlose = input().split()
    iw, il = xs.index(twin), xs.index(tlose) # could optimise to avoid 2 separate index calls if xs is large O_o
    if il < iw:
        xs.remove(tlose)
        xs.insert(iw, tlose)

print(*xs)