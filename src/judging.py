# Judging Troubles
# https://open.kattis.com/problems/judging
# TAGS: dict
# CP4: 2.2e, Sorting, Easier
# NOTES:
"""
Don't need to sort with this approach
"""
N = int(input())

d = {}
for _ in range(N):
    s = input()
    d[s] = 1 + d.get(s, 0)

e = {}
for _ in range(N):
    s = input()
    e[s] = 1 + e.get(s, 0)
    
res = 0
for k, v in d.items():
    res += min(v, e.get(k, 0))

print(res)