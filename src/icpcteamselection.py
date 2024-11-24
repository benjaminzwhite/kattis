# ICPC Team Selection
# https://open.kattis.com/problems/icpcteamselection
# TAGS: logic, mathematics, nice
# CP4: 3.4b, Involving Sorting, E
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/icpcteamselection.md
"""
T = int(input())

for _ in range(T):
    N = int(input())
    xs = sorted(map(int, input().split()))
    res = sum(xs[-2:-2 * N - 1:-2])
    print(res)