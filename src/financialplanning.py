# Financial Planning
# https://open.kattis.com/problems/financialplanning
# TAGS: binary search, greedy
# CP4: 3.3b, Bisection and BSTA, E
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/financialplanning.md
"""
n, target = map(int, input().split())

xs = []
for _ in range(n):
    profit, cost = map(int, input().split())
    xs.append((profit, cost))

lo, hi = 1, 10**11 # TODO: I found the upper limit experimentally that 10**11 works, need to read statement to see if I can determine it from input ranges
while lo < hi:
    mid = (lo + hi) // 2

    total_p, total_c = 0, 0
    for p, c in xs:
        if p * mid > c:
            total_p += p * mid
            total_c += c

    if total_p - total_c >= target:
        hi = mid # guess a lower number of days since can reach target with this number of days, mid
    else:
        lo = mid + 1

print(lo)