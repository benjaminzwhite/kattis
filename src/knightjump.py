# Knight Jump
# https://open.kattis.com/problems/knightjump
# TAGS: bfs, grid
# CP4: 4.4c, Knight Moves
# NOTES:
"""
Just BFS
"""
from collections import deque

N = int(input())
board = []
for _ in range(N):
    board.append(input())

r, c = next((r_, c_) for r_, row in enumerate(board) for c_, cell in enumerate(row) if cell == 'K')
MOVES = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if abs(dr) + abs(dc) == 3]
seen = set()

q = deque([((r, c), 0)])
found = False
while q:
    (r, c), curr_moves = q.popleft()
    
    if (r, c) in seen:
        continue
    
    if (r, c) == (0, 0):
        found = True
        break

    seen.add((r, c))
    
    for dr, dc in MOVES:
        if (0 <= (r_ := r + dr) < N) and (0 <= (c_ := c + dc) < N) and (r_, c_) not in seen and board[r_][c_] != '#':
            q.append(((r_, c_), curr_moves + 1)) 

if found:
    print(curr_moves)
else:
    print(-1)