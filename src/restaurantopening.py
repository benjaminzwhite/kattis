# Restaurant Opening
# https://open.kattis.com/problems/restaurantopening
# TAGS: geometry, logic, nice
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
"""
Nice exercise if you try to improve on brute force approach:

It seems (given easy rating) that the intention is for this problem to be solved with brute force,
corresponding to O(n**4) complexity.

You can actually solve in O(n**2 * log n) which is what I have done below - the basic insight is to realise
that the optimum solution is determined by the median of coordinates.

Note: these medians are taken separately on x and then y axis - the x and y distances don't "interact".

If there were only 1 person per cell, you would get the median_of_xs, median_of_ys by using the x and y values "as-is"

However, there are more than 1 person per cell which means that the cells are "weighted" in importance
by the number of people on them:
A simple way to model this, is to therefore pretend there are "P" copies of each (x, y) where P is the
number of people on that cell, this will have the effect of weighting the medians appropriately. So for
example if there are 510 people on (x=2,y=7) you would pretend that xs = [2,2,2,.....2] <- 510 times.

Then sort these "extended" xs and ys values and take the MEDIAN OF EACH:
-> the total amount of x movement is (x - x_median) for all cells, same for y
"""
n, m = map(int, input().split())

board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

# finding medians - model population at each location as N copies of that location
xs = []
ys = []
for r, row in enumerate(board):
    for c, cell in enumerate(row):
        for _ in range(cell):
            xs.append(c)
            ys.append(r)

xs = sorted(xs)
ys = sorted(ys)

if not xs or not ys:
    print(0)
else:
    median_x = xs[len(xs)//2]
    median_y = ys[len(ys)//2]

    res_x = sum(abs(x - median_x) for x in xs )
    res_y = sum(abs(y - median_y) for y in ys )

    print(res_x + res_y)