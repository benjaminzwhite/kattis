# Lamps
# https://open.kattis.com/problems/lamps
# TAGS: brute force
# CP4: 3.2g, Try All Answers
# NOTES:
from math import ceil

h, P = map(int, input().split())
for hour in range(8000 + 1):
    incan_cost = 60 * hour * P / 100_000 + 5 * ceil(hour / 1000)
    low_cost = 11 * hour * P / 100_000 + 60
    if low_cost < incan_cost:
        print(ceil(hour / h))
        break