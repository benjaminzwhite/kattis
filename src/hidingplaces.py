# Hiding Places
# https://open.kattis.com/problems/hidingplaces
# TAGS: bfs, chess, grid
# CP4: 3.2h, Math Simulation, Easier
# NOTES:
"""
Chess moves with Knight, basically BFS find the most moves needed to reach a/several squares given a starting position

However, quite a bit of work compared to most easy-ranked problems, plus need to consider:
- a sort step at end, so that you get in ascending row and col order
- then must map to rank/file notation also
"""
from collections import deque

MOVES = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if (abs(dr) + abs(dc) == 3)]

cols = "abcdefgh"
rows = "87654321"

T = int(input())

for _ in range(T):
    start = input()

    c, r = cols.index(start[0]), rows.index(start[1])
    seen = set()
    q = deque([ ((r,c), 0)])
    hiding = []
    max_d = 0

    while q:
        (r, c), d = q.popleft()
        
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if d > max_d:
            max_d = d
            hiding = [(r, c)]
        elif d == max_d:
            hiding.append((r, c))

        for (dr, dc) in MOVES:
            if 0 <= (r_ := r + dr) < 8 and 0 <= (c_ := c + dc) < 8:
                q.append( ((r_, c_), d + 1) )

    hiding = sorted(hiding)
    res = []
    for (r, c) in hiding:
        res.append(cols[c] + rows[r])

    print(max_d,' '.join(res))