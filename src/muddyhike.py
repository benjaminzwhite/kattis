# Muddy Hike
# https://open.kattis.com/problems/muddyhike
# TAGS: graph, tree, MST
# CP4: 4.3b, MST, Variants
# NOTES:
"""
MST, this is a kind of Prim's algorithm approach.
Halim calls it on p219 of book the "MiniMax/MaxiMin" variant
"""
from queue import PriorityQueue

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
seen = [[False] * C for _ in range(R)]

pq = PriorityQueue()

for r in range(R):
    pq.put((board[r][0], r, 0)) # start queue with all left side locatiosn
    seen[r][0] = True

res = 0
while not pq.empty():
    w, r, c = pq.get()
    res = max(res, w)
    if c == C - 1: # reached the right side of the board[]
        break
    seen[r][c] = True
    for dr, dc in MOVES:
        if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and not seen[r_][c_]:
            pq.put((board[r_][c_], r_, c_))

print(res)
