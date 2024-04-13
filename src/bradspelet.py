# The Board Game aka Bradspelet
# https://open.kattis.com/problems/bradspelet
# TAGS: dynamic programming, game, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: resolve with a proof/game analysis. Currently solve with dynamic programming logic.

---

To win you must force your opponent to choose between 2 losing options:

e.g. 2x1 is a win for you because you give your opponent 1x1 and 1x1 and both are losing
e.g. 3x1 is a loss for you because you give your opponent 1x1 and 1x2; AND at least one of those options (1x2, solved earlier) is a WINNING OPTION (for them)

The simplest base case to study is 1x1 which we know is losing option so start dp from that state : dp[1][1] = False
"""
dp = [[None] * 101 for _ in range(101)]

dp[1][1] = False # 1x1 is losing

for r in range(1, 101):
    for c in range(r, 101): # note r,c symmetric so can only do upper triangular part of dp board and assign same result to opposite c,r <=> r,c
        # try all possible ways of dividing a r,c board into 2 boards: r,c_ + r,c - c_   (r doesnt change, try all c cuts) or r_,c + r-r_,c (c doesnt change try all r cuts)
        # we are looking for a division into 2 boards such that both resulting boards ARE KNOWN TO BE LOSING (i.e. == False)
        if any((dp[r][c_] == False and dp[r][c - c_] == False) or (dp[r_][c] == False and dp[r - r_][c] == False) for r_ in range(1, r + 1) for c_ in range(r_, c + 1)):
            dp[r][c] = dp[c][r] = True
        else:
            # if there is no division into 2 boards such that both are losing, then all your divisions lead to a winning position for OPPONENT so this board state is LOSING
            dp[r][c] = dp[c][r] = False

n, m = map(int, input().split())

print("A" if dp[n][m] else "B")