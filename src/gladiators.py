# Gladiators
# https://open.kattis.com/problems/gladiators
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/gladiators.md
"""
M_MAX = 105
K_MAX = 105

dp = [[0] * K_MAX for _ in range(M_MAX)]
dp[0][0] = 1
for m in range(1, 101):
    for k in range(101):
        dp[m][k] = dp[m - 1][k - 1] * (2 * m - k - 1) + dp[m - 1][k] * (k + 1)

T = int(input())
for _ in range(T):
    m, k_ = map(int, input().split())
    # k_ is off by one compared to "usual" k (see NOTES) w.r.t to usual Eulerian definition
    print(dp[m][k_ - 1])