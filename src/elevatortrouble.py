# Elevator Trouble
# https://open.kattis.com/problems/elevatortrouble
# TAGS: BFS, improve
# CP4: 4.4a, SSSP, BFS, Easier
# NOTES:
"""
TODO: IMPROVE - is there a proof/mathematics solution ?
"""
from collections import deque

floors, start, goal, up, down = map(int, input().split())
seen = set()
q = deque([(start, 0)])

flg = False
while q:
    curr_floor, moves = q.popleft()
    if curr_floor == goal:
        flg = True
        print(moves)
        break
    if curr_floor in seen:
        continue
    seen.add(curr_floor)
    for delta in up, -down:
        if 0 < (new_floor := curr_floor + delta) <= floors:
            q.append((new_floor, moves + 1))

if not flg:
    print("use the stairs")