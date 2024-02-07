# Arm Coordination
# https://open.kattis.com/problems/armcoordination
# TAGS: geometry, logic
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
Output needs to be in either a clockwise or anticlockwise order for any 4 chosen points and any starting point.
"""
x, y = map(int, input().split())
r = int(input())

for dx, dy in [(-r, -r), (-r, r), (r, r), (r, -r)]:
    print(x + dx, y + dy)