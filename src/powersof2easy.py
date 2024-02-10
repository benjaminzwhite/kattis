# Powers of 2 (Easy)
# https://open.kattis.com/problems/powersof2easy
# TAGS: brute force, binary
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
n, e = map(int, input().split())

s = str(2**e)

res = sum(s in str(x) for x in range(n + 1))

print(res)