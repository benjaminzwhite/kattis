# Appalling Architecture
# https://open.kattis.com/problems/appallingarchitecture
# TAGS: array, grid
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
The logic is straightforward, it's mainly handling confustion about relevant x-coordinate being
0, 1, 2, ... or 0.5, 1.5, 2.5, ... or 1, 2, 3, ... depending on what you are calculating etc.

For the given inputs, I'm calling the "x_left" of the 1x1 box its index in the enumerated row, so its "x_right"
is just x_left + 1.

Basically the centre of mass of a 1x1 box is at x_left + 0.5 <--- hence why we += sum_xs by x_coord + 0.5
That's for the calculation of the mass distribution of the building.

Then for the "base points", the LEFTMOST x POINT is the left_x value of the coordinates of the leftmost box
HOWEVER THE RIGHTMOST x POINT it the *RIGHT_X* value of the coordinates of the rightmost box, i.e. rightmost = x_coord + 1

---

Implementation note:

You don't need to actually store the board[] array, you can just process inputs on the fly I realised after submitting
"""
h, w = map(int, input().split())

board = []
for _ in range(h):
    board.append(input())

sum_xs = 0
weight = 0
for row in board:
    for x_coord, cell in enumerate(row):
        if cell != '.':
            weight += 1
            sum_xs += x_coord + 0.5 # CENTRE OF MASS OF AN ACTUAL 1x1 BOX

# Get the leftmost and rightmost "edges" of the building
for x_coord in range(w):
    if board[-1][x_coord] != '.':
        leftmost = x_coord # LEFTMOST PART OF AN ACTUAL 1x1 BOX
        break

# iterate from right-to-left to get the rightmost "edge"
# CARE! remember to add +1 to the x_coord, as explained in notes above
for x_coord in range(w - 1, -1, -1):
    if board[-1][x_coord] != '.':
        rightmost = x_coord + 1 # RIGHTMOST PART OF AN ACTUAL 1x1 BOX
        break


# numerical optimisation:
# should compare sum_xs to weight * leftmost and to weight * rightmost (to avoid division operation)
# but this is show clearly the appearance of the centre of gravity
centre_of_gravity = sum_xs / weight

if centre_of_gravity < leftmost:
    print("left")
elif centre_of_gravity > rightmost:
    print("right")
else:
    print("balanced")