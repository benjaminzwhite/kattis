# Inflation
# https://open.kattis.com/problems/inflation
# TAGS: sorting, greedy
# CP4: 3.4a, Greedy (Classical)
# NOTES:
n = int(input())

xs = map(int, input().split())

res = float("inf")

for num, denom in zip(sorted(xs), range(1, n + 1)):
    if num > denom:
        res = -1
    else:
        res = min(res, num / denom)
        
print("impossible" if res == -1 else res)