# Eidam-Sand Lair
# https://open.kattis.com/problems/eidamsandlair
# TAGS: logic, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/eidamsandlair.md
"""
T = int(input())
for _ in range(T):
    Yp, Lp, Ys, Ls = map(int, input().split())

    you_to_surface = Yp * Ys

    # Case I/ Lift starts below you - careful, floor numbers are bigger when they are below
    if Lp > Yp:
        lift_to_surface = Lp * Ls

        res = min(you_to_surface, lift_to_surface)

        print(res)
    else:
        # Case II/ Lift starts above you - careful, floor numbers are bigger when they are below
        lift_to_surface = Lp * Ls
        
        # walk to lift, takes time (Yp - Lp) * Ys; then get in lift to surface
        walk_to_lift = (Yp - Lp) * Ys + lift_to_surface
        
        # call lift, takes time (Yp - Lp) * Ls + Yp * Ls
        call_lift = (Yp - Lp) * Ls + Yp * Ls
        
        # you always have the option of walking all the way - see notes for a concrete example
        res = min(walk_to_lift, call_lift, you_to_surface)

        print(res)