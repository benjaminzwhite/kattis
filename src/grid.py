# Grid
# https://open.kattis.com/problems/grid
# TAGS: grid, BFS
# CP4: 4.4a, SSSP, BFS, Easier
# NOTES:
from collections import deque

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(input())

q = deque([(0, 0, 0)])
seen = set()
flg = False

while q:
    r, c, moves = q.popleft()
    if (r, c) in seen:
        continue
    if (r, c) == (R - 1, C - 1):
        print(moves)
        flg = True
        break
    seen.add((r, c))
    k = int(board[r][c])
    for dr, dc in MOVES:
        if 0 <= (r_ := r + k * dr) < R and 0 <= (c_ := c + k * dc) < C:
            q.append((r_, c_, moves + 1))

if not flg:
    print(-1)