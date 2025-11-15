# Permutation Descent Counts
# https://open.kattis.com/problems/permutationdescent
# TAGS: mathematics, combinatorics
# CP4: 3.5h, Non-Classical, 2D, E
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/permutationdescent.md
"""
BIGMOD = 1001113
N_MAX = 105

dp = [[0] * N_MAX for _ in range(N_MAX)]
dp[1][0] = 1

for N in range(2, N_MAX):
    for v in range(N):
        dp[N][v] = dp[N - 1][v] * (v + 1) + dp[N - 1][v - 1] * (N - v) # note should do % BIGMOD here but Python "big int" works without it

T = int(input())
for _ in range(T):
    t, N, v = map(int, input().split())
    print(t, dp[N][v] % BIGMOD) # see comment above, should take modulus earlier