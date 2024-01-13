# Heart Rate
# https://open.kattis.com/problems/heartrate
# TAGS: basic
# CP4: 1.6e, Real Life, Easier
# NOTES:
N = int(input())

for _ in range(N):
    b, p = map(float, input().split())
    print((b - 1) * 60 / p, b * 60 / p, (b + 1) * 60 / p)