# Hydra's Heads
# https://open.kattis.com/problems/hydrasheads
# TAGS: bfs, improve
# CP4: 8.2b, State-Space, BFS, E
# NOTES:
"""
Just did BFS, didn't try solving recurrence - TODO: IMPROVE
"""
from collections import deque

while True:
    H, T = map(int, input().split())
    if (H, T) == (0, 0):
        break

    seen = set()
    q = deque([ ((H, T), 0) ])

    while q:
        (h, t), moves = q.popleft()
        if (h, t) == (0, 0):
            res = moves
            break
        
        if (h, t) in seen:
            continue
        seen.add((h, t))

        if t > 0:
            q.append( ((h, t + 1), moves + 1) )
        if t > 1:
            q.append( ((h + 1, t - 2), moves + 1) )
        if t > 1:
            q.append( ((h - 2, t), moves + 1) )

    print(res)