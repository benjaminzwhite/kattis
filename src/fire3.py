# Fire!
# https://open.kattis.com/problems/fire3
# TAGS: BFS, grid, improve
# CP4: 4.4b, SSSP, BFS, Medium
# NOTES:
"""
TODO: IMPROVE: not satisfied with my implementation, I think it can be done much better.
I still need a seen[][] lookup for the person's cells: I thought at first this could be handled
by checking whether fire had reached the adjacent cells, but my original approach must be incorrect (as I got a TLE)

---

Variant on a BFS, 2 different types of "things" that are being BFS'ed: fire and you.
Fire updates cells first, then you can move.
"""
from collections import deque

MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]

R, C = map(int, input().split())

q_f, q_j = deque([]), deque([])

board = []
for r in range(R):
    row = list(input())
    for c, cell in enumerate(row):
        if cell == 'J':
            q_j.append((r, c, 0))
        if cell == 'F':
            q_f.append((r, c, 0))
        if cell != '#':
            row[c] = float('inf')
    board.append(row)

seen = [[False] * C for _ in range(R)]
res = -1
curr_time = 0
while q_j and res < 0:
    # update fire
    while q_f and q_f[0][2] == curr_time:
        r, c, t = q_f.popleft()
        if board[r][c] < t:
            continue
        board[r][c] = min(board[r][c], t)
        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and board[r_][c_] != '#' and board[r_][c_] > t + 1:
                board[r_][c_] = t + 1
                q_f.append((r_, c_, t + 1))

    while q_j and q_j[0][2] == curr_time:
        r, c, t = q_j.popleft()
        if t + 1 > board[r][c] or seen[r][c]:
            continue
        seen[r][c] = True
        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            res = t + 1
            break
        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and board[r_][c_] != '#' and board[r_][c_] > t + 1:
                q_j.append((r_, c_, t + 1))
    curr_time += 1
    
if res > 0:
    print(res)
else:
    print("IMPOSSIBLE")