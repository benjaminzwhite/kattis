# Zbrka
# https://open.kattis.com/problems/zbrka
# TAGS: mathematics, combinatorics, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/zbrka.md
"""
BIGMOD = 10 ** 9 + 7
N_MAX = 1_005
C_MAX = 10_005

# inputs
N, C = map(int, input().split())

# UPDATE: slight optimization - you can't have more than comb(N, 2) pairs so confusion is bounded by this in any case
C = min(C, N * (N + 1) // 2)

# dp is implementing T(n,k) from notes above.
dp = [[0] * C_MAX for _ in range(N_MAX)]
dp[1][0] = 1 # all (there are cnt=1 of them) sequences with N=1 terms i.e. {1} have confusion 0

for n in range(2, N + 1):
    for k in range(C + 1):
        # dp[n][k] = dp[n][k-1] - dp[n-1][k-n] + dp[n-1][k]
        #                                ^^^^^
        # CARE! need to be careful with the k-n term; it wraps around, and only makes sense (see notes above) if k >= n
        # so only do if k>=n:
        dp[n][k] = dp[n][k - 1] + dp[n - 1][k]
        if k >= n:
            dp[n][k] -= dp[n - 1][k - n]

        dp[n][k] %= BIGMOD

print(dp[N][C] % BIGMOD)