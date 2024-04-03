# Ding Dong Ditch
# https://open.kattis.com/problems/dingdongditch
# TAGS: array, basic
# CP4: 0, Not In List Yet
# NOTES:
from itertools import accumulate

N, Q = map(int, input().split())
xs = sorted(map(int, input().split()))
queries = map(int, input().split())

acc = list(accumulate(xs))

for q in queries:
    print(acc[q - 1])