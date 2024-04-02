# Going to School - also called Skolvagen
# https://open.kattis.com/problems/skolvagen
# TAGS: dynamic programming, dp
# CP4: 0, Not In List Yet
# NOTES:
"""
Practicing the "dynamic programming states and transitions approach" from CP4 book:

You have 2 states: at_top or at_bottom. You start at top with 0 moves or at bottom with +1 move

You take +1 cost for each crossing; and then evaluate if you could have reached the current state by crossing the road (if other location is cheaper) - that's the min(2 options) part

You end in at_top state -> print(top)
"""
s = input()

top, bottom = 0, 1

for c in s:
    if c == "S":
        bottom += 1
    elif c == "N":
        top += 1
    else:
        top += 1
        bottom += 1
    top, bottom = min(top, bottom + 1), min(bottom, top + 1)

print(top)