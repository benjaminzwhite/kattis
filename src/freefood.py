# Free Food
# https://open.kattis.com/problems/freefood
# TAGS: array
# CP4: 2.3c, DAT, Others
# NOTES:
"""
Probably more efficient to do with a boolean array of size 365
"""
N = int(input())

res = set()

for _ in range(N):
    s, t = map(int, input().split())
    res.update(range(s, t+1))

print(len(res))