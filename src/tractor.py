# Tractor
# https://open.kattis.com/problems/tractor
# TAGS: logic, improve
# CP4: 8.3c, Counting Paths, Harder
# NOTES:
"""
TODO: IMPROVE: I can't think of a concise combinatorial/analytical solution for now.

AFAICT you can't just take e.g. the log2 since (look at diagram below) if you put X at (x=5,y=2) there are
points from the "3" generation that are outside the X-rectangle, BUT ALSO POINTS FROM THE "2" GENERATION.

In this case specifically the point (0,3) from generation "2" is outside the rectangle so you can't
naively do an approach like "all_full_generations up to log2 then adjust a bit" AFAICT.
Might need an inclusion-exclusion approach: will think about it later.

---

Just draw the diagram for n = 1,2,3,4
-> you see it defines a "wave like" pattern outwards with lines of constant x+y 0,1,3,7...

   3 . . . . . . . . 
   . 3 . . . . . . .
   . . 3 . . . . . .
   - - - 3 - - X . .  <--- let's say X is the given upper right corner
   2 . . . 3 . | . .
   . 2 . . . 3 | . .
   1 . 2 . . . 3 . .
   0 1 . 2 . . | 3 .

So you want to count how many points are within the X-rectangle:

Note that the "lines" L_0, L_1, L_2, L_3 have equation x+y=0, 1, 3, 7 etc.

So while the X point has (x+y) > current_line, you need to keep generating lines as the points will be within the rectangle

e.g. here with X = (6,4) you DO need to consider x+y=7 line, but NOT x+y=15 line (corresponding to 4th generation, 2**4 - 1 etc)

-> each generation that is "<= X" contributes: 2**n points
   BUT some of them may lie OUTSIDE of the x/y dimensions of the rectangle formed by X:
   in the illustration the "3" point corresponding to (x=7,y=0) and the three "3" points x=0,1,2 y=7,6,5 are outside.

=> SO YOU REMOVE from 2**n points those with y > X's y value, and those with x > X's x value.
   i.e. you remove: in this case: (7 - 6) = 1 and (7 - 4) = 3 points.
"""
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    X_AB = A + B # just to agree with Notes above - X's A+B value is what determines up to which "line"/generation we need to consider
    
    res = 0
    exp = 0
    # line: 0,1,3,7... i.e. the line == x+y constant
    while (line := 2 ** exp - 1) <= X_AB:
        res += 2 ** exp
        res -= max(0, line - A)
        res -= max(0, line - B)
        exp += 1

    print(res)