# Lopsided Lineup
# https://open.kattis.com/problems/lopsidedlineup
# TAGS: logic, proof, nice
# CP4: 3.4c, Involving Sorting, H
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/lopsidedlineup.md
"""
n = int(input())

row_sums = []
for _ in range(n):
    row_sums.append(sum(map(int, input().split())))

row_sums = sorted(row_sums)

losers = sum(row_sums[:n//2])
winners = sum(row_sums[n//2:])

print((winners - losers) // 2)