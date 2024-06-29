# Escape from Enemy Territory
# https://open.kattis.com/problems/enemyterritory
# TAGS: binary search, BFS, nice
# CP4: 8.7b, BSTA+Other, Harder
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/enemyterritory.md
"""
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# -- Inputs --
# CARE!: Exercise inputs uses x, y -> flip to get R, C in right place as my preference instead of y, x
B, C, R = map(int, input().split())
start_c, start_r, end_c, end_r = map(int, input().split()) # CARE! inputs as x,y so we want r,c so take them in as c,r

# Precompute the proximity information for the given input grid by doing BFS
proximity = [[None] * C for _ in range(R)]

bases = deque([])
for _ in range(B):
    bc, br = map(int, input().split()) # CARE! inputs as x,y so we want r,c so take them in as c,r
    bases.append((br, bc))
    proximity[br][bc] = 0

while bases:
    r, c = bases.popleft()
    for dr, dc in MOVES:
        if (0 <= (r_ := r + dr) < R) and (0 <= (c_ := c + dc) < C) and proximity[r_][c_] == None:
            proximity[r_][c_] = proximity[r][c] + 1
            bases.append((r_, c_))

# -- Binary search --
# UPDATE: see notes above about lo = 0 as starting condition for binary search (I had lo = 1 originally but it gives WA/RTE)
lo = 0
hi = R * C # TODO: for initial hi, can you just get the exact value of the highest distance from the bases precompute step earlier?
while lo < hi:
    mid = (lo + hi) // 2

    flg = False 
    
    if proximity[start_r][start_c] >= mid:
        q = deque([(start_r, start_c, 0)])
        seen = [[False] * C for _ in range(R)]
        while q:
            r, c, pathlen = q.popleft()
            if (r, c) == (end_r, end_c):
                flg = True
                res = [mid, pathlen]
                break
            if seen[r][c]:
                continue
            seen[r][c] = True

            for dr, dc in MOVES:
                if (0 <= (r_ := r + dr) < R) and (0 <= (c_ := c + dc) < C) and proximity[r_][c_] >= mid:
                    q.append((r_, c_, pathlen + 1))

    if flg: # CARE! think carefully about the binary search updating conditions here, see notes above.
        lo = mid + 1
    else:
        hi = mid

print(*res)