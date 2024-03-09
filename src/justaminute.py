# Just a Minute
# https://open.kattis.com/problems/justaminute
# TAGS: basic
# CP4: 1.6h, Time, Easier
# NOTES:
T = int(input())

numer = 0
denom = 0

for _ in range(T):
    d, n = map(int, input().split())
    numer += n
    denom += d

res = numer / denom / 60

if res <= 1.0:
    print("measurement error")
else:
    print(res)