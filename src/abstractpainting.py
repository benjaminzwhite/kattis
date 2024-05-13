# Abstract Painting
# https://open.kattis.com/problems/abstractpainting
# TAGS: mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
There are 3 distinct Polya patterns for a single square:

   x       x      y
  x y     y y    x y
   y       x      x

For a single free square, you can pick one of the regions (say x) in 3 ways, then pick the other region, y, in (3-1) = 2 ways

Since there are 3 patterns, there are thus (3*2) * 3 = 18 distinct ways to paint the free single square (matches the given testcase OK)

If you move along first row, the next_square must match its "left edge" with prev_square.

This means that you now can choose: one of the 3 patterns to use, but with only 2 possible colors for the "unfixed/uncolored" region.
-> 6 choices for top row

Same argument for leftmost colum -> 6 choices per square.

Finally for "internal" squares, e.g. say you are in 2nd row and 2nd column now, having filled first row and column as described above:

Your "top" and "left" borders are already fixed by the coloring:

Either: top == left color -> you must therefore be in the (1 out of 3) patterns where bottom==right must have same color, and you have (3-1) == 2 colors
        to assign to bottom+right for a total of 1*2 = 2 ways/
    OR: top != left color -> you must therefore be in the (2 out of 3) patterns where bottom != right, but right==left and bottom==top UNIQUELY 
        FIXES THE "CHOICE" OF COLORS -> only 1 color option for the bottom and right, so you have a total of 2*1 = 2 ways in this case also.
    --> So in ALL CASES, internal squares will always have exactly 2 ways of proceeding.

Summary table:

         R __________________
       C   18  6  6  6  6  6
       |    6  2  2  2  2  2
       |    6  2  2  2  2  2
       |    6  2  2  2  2  2

So the result is 18**1  *   6**(C-1)  *    6**(R-1)   *   2**(C-1)*(R-1)

Quick consistency check: we expect result should be symmetric under R<->C : yes, it is OK

---

Implementation notes:

You can simplify the expressions below a lot to get a much shorter answer if you want to code golf a bit
(All the stuff with R>1 and C>1 is not needed, just left it for clarity to map onto the explanation above)
"""
BIGMOD = 10**9 + 7

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())

    res = 18 # i.e. 18**1 

    if R > 1:
        res *= pow(6, (R - 1), BIGMOD)
    if C > 1:
        res *= pow(6, (C - 1), BIGMOD)
    if R > 1 and C > 1:
        res *= pow(2, (C - 1) * (R - 1), BIGMOD)

    print(res % BIGMOD)