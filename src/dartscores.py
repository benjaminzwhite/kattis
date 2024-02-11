# Dart Scores
# https://open.kattis.com/problems/dartscores
# TAGS: geometry, basic
# CP4: 7.2c, Circles
# NOTES:
"""
CARE! need to handle out-of-board check (the check: tmp > 11 in my code corresponds to outside of last largest circle)
"""
from math import ceil

T = int(input())

for _ in range(T):
    n = int(input())
    res = 0
    for _ in range(n):
        x, y = map(int, input().split())
        r = (x * x + y * y)**0.5
        tmp = ceil(r / 20)
        if tmp == 0:
            res += 10
        elif tmp > 11:
            continue
        else:
            res += (11 - tmp)

    print(res)