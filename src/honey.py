# Honeycomb Walk
# https://open.kattis.com/problems/honey
# TAGS: mathematics, combinatorics, dynamic programming, improve
# CP4: 5.4d, Others, Easier
# NOTES:
"""
TODO: IMPROVE: Solved with dynamic programming, probably can derive a combinatorial formula

---

Resources for hexagonal grid:

https://www.redblobgames.com/grids/hexagons/
https://math.stackexchange.com/questions/2254655/hexagon-grid-coordinate-system
"""
MAX_N = 30  # we will place center of honeygrid in the "center" of our 2d grid such that it is large enough for walks of n<=14 steps
# 30 seems enough so that there no hexagonal path that reaches the edge of the dp grid. We put the origin at x,y = 30//2, 30//2.

# learnt from https://www.redblobgames.com/grids/hexagons/ how to encode hex grid in 2d grid
MOVES = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1)]

dp = [[[0 for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)]

x_orig = MAX_N // 2
y_orig = MAX_N // 2

dp[0][x_orig][y_orig] = 1 

for steps in range(1, MAX_N):
    for x in range(1, MAX_N):
        for y in range(1, MAX_N):
            dp[steps][x][y] = sum(dp[steps - 1][x + dx][y + dy] for dx, dy in MOVES)

T = int(input())
for _ in range(T):
    n_steps = int(input())
    print(dp[n_steps][x_orig][y_orig])