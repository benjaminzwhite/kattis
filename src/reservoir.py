# Reservoir
# https://open.kattis.com/problems/reservoir
# TAGS: binary search, stack, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/reservoir.md
"""
from bisect import bisect_left

T = int(input())
for _ in range(T):

    N = int(input())
    xs = list(map(int, input().split()))
    hs = list(map(int, input().split()))

    # --- PRECOMPUTE ---
    # Get all the available volume at each barrier, compute this once with the given xs, hs
    # Append results to a LOOKUP: VOLS_AT_BARRIERS
    # ------------------
    stk = [(-1, 0, float('inf'))] # init dummy value, infinitely high with right x == 0 (THIS NEVER GETS POPPED FROM STACK)

    ts = [] # update: probably don't need to create this list, can just iterate over the zip (xs, hs) directly, but it's clearer to see
    for (x, h) in zip(xs, hs):
        ts.append((x, x + 1, h))  # LEFT x, RIGHT x' = x+1, HEIGHT

    VOLS_AT_BARRIERS = []
    total_vol = 0
    for barrier, (R_left, R_right, R_h) in enumerate(ts, 1):
        if R_h < stk[-1][2]:
            avail_vol = R_h * (R_left - stk[-1][1])
            total_vol += avail_vol
            stk.append((R_left, R_right, R_h))
            VOLS_AT_BARRIERS.append(total_vol)
        else:
            # NOTE: extra notes after submitting [draw this to understand]
            # as you pop the elements whose height is smaller than curr barrier, moving leftwards, you MUST NOT ADD THE "FULL VOLUME"
            # of each prev_barrier->curr_barrier
            # because you have already added a portion of that volume in intermediate barriers
            # [DRAW A DRAWING WITH E.G barrier heights = 10,5,3,1,8] -> when you start stk pop you process 1->8, which contributes a small
            # rectangle, then when you process 3->8 , you do NOT use 3 as the height because there is already:
            # a) the volume from 3 DOWN TO 1 that was added when you processed step 3->1
            # b) the volume from 1 UP TO 8 that was just added during the ongoing stack popping steps
            # --> again if you draw this you see easily that you just need to adjust the "effective" height of each stack pop barrier
            #     by an amount equal to the height of the PREVIOUSLY POPPED BARRIER (init to 0 since the very first smaller barrier has "full effective height")
            prev_height = 0
            while R_h >= stk[-1][2]:
                L_left, L_right, L_h = stk.pop()
                avail_vol = (L_h - prev_height) * (R_left - L_right)
                prev_height = L_h
                total_vol += avail_vol
            # NOTE:
            # Important - when you get here [draw it] you have popped all the smaller barriers than current barrier
            # THEREFORE, YOU ARE NOW IN A SITUATION WHERE THE CURR BARRIER ITSELF IS THE SMALLER ONE
            # -> SO (draw it) YOU NEED TO ALSO ADD THE VOLUME BETWEEN THIS CURR BARRIER AND THE BIGGER ONE TO ITS LEFT 
            # e.g. imagine 1000,8,5,3,200
            # you pop 3,5,8 and now get to 1000 -> whatever the width between 1000 and 200 was, call it W
            # you now have to add the avail_vol corresponding to: HEIGHT = 200 - 8 <--- because 8 is the PREV_HEIGHT
            # and using width = W (again taking care of using the right side of 1000 and the left side of 200) etc.
            # ------------------
            # ONE LAST RANGE TO PROCESS, UP TO THE CURRENT STACK TOP: USE THIS ELEMENTS HEIGHT AND PREV HEIGHT
            avail_vol = (R_h - prev_height) * (R_left - stk[-1][1])
            total_vol += avail_vol
            VOLS_AT_BARRIERS.append(total_vol)
            stk.append((R_left, R_right, R_h))

    # --- END PRECOMPUTE ---
    # Now just binary search for each query
    Q = int(input())
    for _ in range(Q):
        query = int(input())
        
        res = bisect_left(VOLS_AT_BARRIERS, query) # Python magic

        print(res)