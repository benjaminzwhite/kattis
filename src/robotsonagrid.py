# Robots on a Grid
# https://open.kattis.com/problems/robotsonagrid
# TAGS: DFS, grid, dynamic programming, improve
# CP4: 4.6b, Counting Paths, Easier
# NOTES:
"""
TODO: IMPROVE: my solution doesn't TLE but it runs slow (I'm guessing the DFS on N=1000 case) maybe a better way to solve ?
"""
BIGMOD = 2**31 - 1

N = int(input())
board = []
for _ in range(N):
    board.append(input())

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if board[r][c] != '#':
            if r > 0:
                dp[r][c] += dp[r - 1][c]
            if c > 0:
                dp[r][c] += dp[r][c - 1]

flg = (dp[-1][-1] > 0)
if flg:
    print(dp[-1][-1] % BIGMOD)

can_dfs = False
if not flg:
    stk = [(0, 0)]
    MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    seen = [[False] * N for _ in range(N)]
    while stk:
        r, c = stk.pop()
        if (r, c) == (N - 1, N - 1):
            can_dfs = True
            break
        if seen[r][c]:
            continue
        seen[r][c] = True
        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < N and 0 <= (c_ := c + dc) < N and board[r_][c_] != '#' and not seen[r_][c_]:
                stk.append((r_, c_))
if can_dfs:
    print("THE GAME IS A LIE")

if not flg and not can_dfs:
    print("INCONCEIVABLE")