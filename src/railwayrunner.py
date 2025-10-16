# Railway Runner
# https://open.kattis.com/problems/railwayrunner
# TAGS: dfs, grid
# CP4: 0, Not In List Yet
# NOTES:
"""
Standard maze dfs/moves type stuff but hard to understand some of the rules though: you CANNOT move laterally onto a ladder etc.
"""
R = int(input())
board = [input() for _ in range(R)]

MOVES = {'*': {(0, -1): '*', (0, 1): '*', (1, 0): '*.'}, '.': {(0, -1): '.', (0, 1): '.', (1, 0): '/.'}, '/': {(1, 0):'*'}}

flg = False

stk = [(0, c, '.') for c in range(3) if board[0][c] == '.']

seen = [[False] * 3 for _ in range(R)]

while stk:
    r, c, cell = stk.pop()
    if r == R - 1:
        flg = True
        break
    if seen[r][c]:
        continue
    seen[r][c] = True

    for (dr, dc), req in MOVES[cell].items():
        if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < 3 and (adj := board[r_][c_]) in req:
            stk.append((r_, c_, adj))

if flg:
    print("YES")
else:
    print("NO")