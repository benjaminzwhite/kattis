# Space Race
# https://open.kattis.com/problems/spacerace
# TAGS: basic
# CP4: 1.4n, Still Easy
# NOTES:
n = int(input())
d = float(input())

tmp = float('inf')

for _ in range(n):
    x, _, r = input().split()
    r = float(r)
    if r < tmp:
        tmp = r
        res = x

print(res)