# Getting Gold
# https://open.kattis.com/problems/gold
# TAGS: grid, DFS, nice
# CP4: 4.2b, Flood Fill, Easier
# NOTES:
"""
Nice exercise/variant - it's basically a mini Wumpus World O_o but easier than I thought

Basically, once you reach a given point in the board, you CAN move from that cell IF AND ONLY IF there are NO 'T-cells' adjacent to you
because if there is a Trap T anywhere it creates the wind in your current cell and you can't move with 100% certainty.

So it's Flood Fill except in addition to checking for walls, #, you DO NOT add all (1,2,3 or 4) neigboring cells INDEPENDENTLY but rather you
consider ALL NEIGHBORING CELLS AS A GROUP AND ONLY EXTEND YOUR BFS/DFS QUEUE/STK IF *ALL CANDIDATE MOVES* ARE OK i.e. trap free.
"""
W, H = map(int, input().split())

board = []
for _ in range(H):
    board.append(input())

r, c = next((r, c) for r, row in enumerate(board) for c, cell in enumerate(row) if cell == 'P')

stk = [(r, c)]
seen = set()
res = 0
MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

while stk:
    r, c = stk.pop()
    if (r, c) in seen:
        continue

    seen.add((r, c))
    if board[r][c] == 'G':
        res += 1

    candidates = []
    for dr, dc in MOVES:
        if 0 < (r_ := r + dr) < H - 1 and 0 < (c_ := c + dc) < W - 1 and board[r_][c_] != '#':
            candidates.append((r_, c_))
    if all(board[r_][c_] != 'T' for r_, c_ in candidates):
        stk.extend(candidates)

print(res)