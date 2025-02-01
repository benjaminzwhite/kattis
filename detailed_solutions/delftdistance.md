# Detailed solution for Kattis - Delft Distance

[Problem statement on Kattis](https://open.kattis.com/problems/delftdistance)

This is a really nice exercise - the logic is fairly standard dynamic programming, but finding a clever implementation to deal with the grid layout is a very interesting challenge.

## Tags

dynamic programming

## Solution

The logic/paper answer: it's Manhattan distance at first - without any `O` the answer would be independent of path, you just take `R+C` steps total.

But, similar to classic dp exercise where you have "holes" in a `R*C` grid and need to calculate paths that avoid the holes, here the optimal
answer is clearly to take that path that touches as many `O` as possible, including moving between `OO` and `OO_vertical` etc., as this always
reduces total distance. So the solution is an "inverse" to the above classic dp exercise - we want to calculate **the path that touches as many circles as possible**.

Now for the implementation tricky stuff - the grid is no longer a nice regular lattice, and at first I was trying to have mixed-length rows and keep
track of various offsets but it's a nightmare (like "if row 3 has 8 circles, then look-behind is some function f(3,8)" etc.)

So while thinking about how to work with "not nice grids", I thought at first of those hexagonal problems where you have to convert easy BFS to
non traditional coordinates, but then I was reminded of an even better relevant example from previous solved exercises:

[Diagonal Cut - https://open.kattis.com/problems/diagonalcut](https://open.kattis.com/problems/diagonalcut)

which I've solved in a few different ways: same kind of logic, or "problemsolving intuition" which is in general that "you should work with what is easy
for you, not necessarily the input as it is given" (same kind of intuition as transforming coordinate system, rotating visualizatin, introducing dummy points in graphs etc.)

So, returning to this exercise: **the nice idea is to use a 2x2 "mesh" instead of the board as given**:

I divide the grid by 2x2 to get points that are easier to work with for (can't draw in ASCII, too complex, just use pen and paper or read the comments in code below also).

In addition to the "regular" 4 vertices of each gridsquare, **add the 4 half-length ones, and the centre of each square**. These centre points are the nice
addition, as - **if you initialize them to `inf` in the dp** - they a) allow you to have same-size rows and cols but b) never interfere with "real" calculations as they will always contribute `inf` to any min() dp calculation so will never be "valid options" for the path dp calculation.

### Implementation/important detail:

The other really nice thing I discovered during implementation is that, no matter where you are "geometrically" when considering the dp options for the circle case (i.e. you are calculating dp cost to reach any point or "half-point" on the mesh), what you find is that **the 3 dp options are always at the same relative position - left/above/aboveleft, and in all configurations the "unphysical" cases are handled**. I made separate notes for this as I was surprised that it works out cleanly, see notes in code below.

The other tricky thing is to map back, from a given mesh location, to finding the geometry of where you really are in the board of `O` and `X`: if you let `r,c` be coordinates in the **mesh grid**, then the coords in the input `board[]` are given by `(r-1)//2` and `(c-1)//2` - you need the `-1` because the top row (`r=0`) and col (`c=0`) of the mesh **are not below/to the right of anything** (again, draw a `R*C` grid with both coordinate systems if you need to clarify this, easy to visualize on paper)


## AC code

```python
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
```
