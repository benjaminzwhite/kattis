# Conquest Campaign
# https://open.kattis.com/problems/conquestcampaign
# TAGS: grid, BFS
# CP4: 4.4b, SSSP, BFS, Harder
# NOTES:
"""
Implementation note:

CARE! 1-based indexing.

BFS, but return day-1 since you will overshoot by 1 with this implementation (the last cell to add will not yet be in seen
so it will be added with day_ = day+1 but then wont actually have any neighbors to propagate this day+1 value to, meaning 
it was the last of the previous_day_reached values)
"""
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, N = map(int, input().split())

q = deque([])
for _ in range(N):
    r, c = map(int, input().split())
    q.append((r - 1, c - 1, 1)) # 1 based indexing O_o

seen = set()

while q:
    r, c, day = q.popleft()
    if (r, c) in seen:
        continue
    seen.add((r, c))
    for dr, dc in MOVES:
        if 0 <= (r_ := r + dr) < R and 0 <= (c_ := c + dc) < C:
            q.append((r_, c_, day + 1))

print(day - 1)