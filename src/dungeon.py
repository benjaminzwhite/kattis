# Dungeon master
# https://open.kattis.com/problems/dungeon
# TAGS: grid, bfs
# CP4: 4.4b, SSSP, BFS, Harder
# NOTES:
"""
Just a 3d BFS
"""
from collections import deque

MOVES = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0)]

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    board = []
    for l in range(L):
        level = []
        for r in range(R):
            curr = input()
            for c, x in enumerate(curr):
                if x == 'S':
                    start_l, start_r, start_c = l, r, c
                if x == 'E':
                    end_l, end_r, end_c = l, r, c
            level.append(curr) 

        board.append(level)

        input() # CARE: empty line, due to input format O_o

    q = deque([(start_l, start_r, start_c, 0)])
    seen = set()
    res = None
    while q:
        l, r, c, cnt = q.popleft()
        if (l, r, c) in seen:
            continue
        if (l, r, c) == (end_l, end_r, end_c):
            res = cnt
            break
        
        seen.add((l, r, c))

        for (dl, dr, dc) in MOVES:
            if 0 <= (l_ := l + dl) < L and 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C and board[l_][r_][c_] != '#':
                q.append((l_, r_, c_, cnt + 1))

    if res is None:
        print("Trapped!")
    else:
        print(f"Escaped in {res} minute(s).")