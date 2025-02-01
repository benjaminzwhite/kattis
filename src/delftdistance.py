# Delft Distance
# https://open.kattis.com/problems/delftdistance
# TAGS: dynamic programming, nice
# CP4: 4.6a, S/Longest Paths on DAG
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/delftdistance.md
"""
from math import pi

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(input())

dp = [[float('inf')] * (2 * C + 1) for _ in range(2 * R + 1)] # 2* because we use 2x2 mesh size
# See notes: CARE! Above, you need the +1, otherwise don't get rightmost and bottommost mesh points

MESH_R, MESH_C = len(dp), len(dp[0])
for r in range(MESH_R):
    dp[r][0] = r * 5 # 10 is square length so half length is 5 to each intermediate point
for c in range(MESH_C):
    dp[0][c] = c * 5 # 10 is square length so half length is 5 to each intermediate point

for r in range(1, MESH_R):
    for c in range(1, MESH_C):
        # check if in a "centre" point of the mesh grid i.e within a square or circle
        # IF SO: leave the dp as INF, so that this "unphysical/impossible option" is never chosen
        if r % 2 == 1 and c % 2 == 1:
            continue

        # lookup what is "in" the current square at the right location:
        BOARD_ROW, BOARD_COL = (r - 1) // 2, (c - 1) // 2
        if board[BOARD_ROW][BOARD_COL] == 'X':
            # if we have a X to our left, or above, or aboveleft, then can only get here by +5 distance from  or from "left":
            dp[r][c] = min(5 + dp[r - 1][c], 5 + dp[r][c - 1])
            # note however that, depending on geometry, if we are on a half-mesh point where "above" is the centre of a Square/X, then its dp value is INF
            # same for if we are on a half-mesh point where "left" is centre of a square:
            # this dp code above handles both case where you end up on inf square since this will never be taken as option due to the min()
        else:
            #if we have a O to our left, or above, or aboveleft, then we have 3 OPTIONS NOT JUST 2:
            dp[r][c] = min(5 + dp[r - 1][c], 5 + dp[r][c - 1], 5 * pi / 2 + dp[r - 1][c - 1])
            # HERE IS THE INTERESTING CASE:
            # draw a drawing if you can't visualise again:
            # when you are on a half-mesh point, and you have a O to your left, aboveleft, or above:
            # you can either reach curr location from a "straight halfsegment to a delta_r or delta_c = 1" 
            # OR a "quarter radius with a delta_r AND delta_c BOTH = 1"
            # NOTE THAT IN GENERAL, YOU ONLY HAVE "2 of the 3" REAL OPTIONS, but again the 3rd option will end up being in the centre of the O and will have dp value INF
            # basically the above code handles the geometry whether your mesh point is "bottom middle" of a circle O or "right middle" of a circle O:
            #
            # ILLUSTRATION OF 3x3 GRID POINTS IN A GIVEN MESH REGION AROUND A "REAL" circle / square from input board:
            #
            #          Z  
            #    . ___ . ___ . X
            #    |           | 
            #    |  CIRCLE   |
            #  V .     .     . A <---- here at A the 3 dp options are: above: dp[r-1][c], STRAIGHT LINE TO "REAL" POINT X
            #    | Y:dp=inf  |                                         left:  dp[r][c-1], STRAIGHT LINE TO "DUMMY/MESH" POINT Y, which has dp=inf unchangable
            #    |           |                                    aboveleft:  dp[r-1][c-1], CURVELINE TO "REAL" POINT Z VIA A QUARTER CIRCLE DISTANCE
            #    .____ . ___ . 
            #  U      C       B
            #                 ^^____ here at B the 3 dp options are A: dp[r-1][c], straighline to real point A, dp[r][c-1], straightline to realpoint C, and dp[r-1][c-1] "curveline" to centre point Y BUT THIS WONT BE TAKEN SINCE ITS DP is INF, SO CODE HANDLES IT BECAUSE THIS "CURVELINE" IS NOT IN FACT A REAL OPTION
            #
            #
            # Finally, at C: 3 dp options are dp[r][c-1] straighline to realpoint U, dp[r-1][c] straigtline to DUMMY POINT Y, and dp[r-1][c-1] WHICH IS INDEED A REAL VALID CURVE LINE AROUND THE CIRCLE THIS TIME AND LANDS AT RIGHT LOCATION, V, ON THE MESH.

res = dp[-1][-1]

print(res)