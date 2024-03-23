# Malfunctioning Robot
# https://open.kattis.com/problems/malfunctioningrobot
# TAGS: logic, geometry
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
Nice little exercise: Manhattan distance with a twist, see notes in code below.
"""
T = int(input())

for _ in range(T):
    # can do -1, -1 reduce distance with _| steps
    x1, y1, x2, y2 = map(int, input().split())

    # so get to same horiz or vertical in delta _| movements i.e. delta*2 actual steps
    delta = min(abs(x1 - x2), abs(y1 - y2))
    remainder = max(abs(x1 - x2), abs(y1 - y2)) - delta
    res = 2 * delta

    # do the remainder in a "straightline" _|-|_|-|_ etc
    if remainder % 2 == 0:
        res += (remainder // 2) * 4  # _|-| 4 per repeat unit
    else:
        res += (remainder // 2) * 4 + 1 # _|-|_ 4 per repeat unit plus one final single _ to reach

    print(res)