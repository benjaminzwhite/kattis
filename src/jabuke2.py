# Jabuke
# https://open.kattis.com/problems/jabuke2
# TAGS: BFS, nice
# CP4: 8.2c, State-Space, BFS, H
# NOTES:
"""
Nice BFS variant - the trick is that you can reuse your SEEN[] lookup table:

- instead of recreating the R*C list for EACH GENERATION, just assign SEEN[r][c] to equal 'g' for each query g=1,2,3....
- then, instead of looking up whether SEEN[r][c] == True, you are checking if it is == the CURRENT value of g

i.e. SEEN[r][c] == 4 means that we have updated SEEN[r][c] at generation 4 (so if you are in generation 5,6,7...2471, whatever...)
then it is as if it is FALSE since it is an "older BFS" that accessed this point, not the current one
"""
from collections import deque

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)] # convert so list so can update/assign 'x' to [r][c]

seen = [[0] * C for _ in range(R)]

MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]

G = int(input())
for g in range(1, G + 1):
    y, x = map(int, input().split())
    start_r, start_c = y - 1, x - 1 # CARE! 1 based indexing; also don't confuse rows/columns (my terminology) with x,y etc.

    q = deque([(start_r, start_c)])
    res = float('inf')
    while q:
        r, c = q.popleft()

        if seen[r][c] == g:
            continue
        seen[r][c] = g

        if (start_r - r) ** 2 + (start_c - c) ** 2 >= res:
            continue

        if board[r][c] == 'x': # CARE! LOWERCASE x
            res = min(res, (start_r - r) ** 2 + (start_c - c) ** 2)
            if res == 0: # can't do better so break early
                break

        for dr, dc in MOVES:
            if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C:
                q.append((r_, c_))

    board[start_r][start_c] = 'x'
    print(res)