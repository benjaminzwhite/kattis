# Detailed solution for Kattis - Cake

[Problem statement on Kattis](https://open.kattis.com/problems/cake)

Nice little puzzle - you can always tile it perfectly, but "explaining to the computer" is a bit hard O_o

## Tags

array, logic

## Solution

Basically at any moment consider the topmost **row** (think of this as the row which has point(s), such that there are NO POINTS in rows above this row).

You want to draw a horizontal line under this row -> WLOG you can draw this horizontal line "as low down as possible". What does this mean? **Until the next row which does contain a point**.

It's very easy when you draw it on paper, the solution is immediate - but hard to ascii O_o

```
       . . . . . . .
       . . . . O . . <-- current topmost row
       . . . . . . .
       . . . . . . . _______ this is down to where you can extend the topmost rows' "bottom line"
       . O . . . O .
```

Each time you do this, you basically end up with a smaller subproblem (you solve the board with the given bottom line, and are left with a smaller rectangle/fewer rows which can be solved by hypothesis)

Now, for the **columns**, if there are multiple points in the current topmost row:

```
      . . O . . . O . O O . . . _______ this is the current "bottom line" (here we have a 1xC block, to avoid drawing empty rows)
```

You start with the leftmost border in col=1, then for each point O, move the rightmost boarder such that it just includes that point in the obvious way:

```
      . . O|. . . O|. O|O|. . .

                         ^-------- EXCEPT THIS ONE!! This is the only tricky part, it should be O|O . . .| instead
```

The tricky part is that the **last point on the row** should be extended all the way to the full/final (C)olumn width. (This ensures that the "vertical" slices use up the entire current subrectangle, ie avoids unused space, and allows to proceed with the recursive proof that any rectangle can be solved with 0 leftover).

### Implementation notes

Solution should be self explanatory below, process rows and for each row, go through its sorted points from left to right column values, taking care for the **last point in the row**.

CARE! possibility for error: problem wants the rectangle defined by opposite corners **with smaller row,col before larger row,col** and with **mixed coords: r1 c1 r2 c2**

While testing, some good test cases are ones where e.g. you have 4 points in the bottom left corner:

R,C = 6,8 and points are 5,1 5,2 6,1 6,2 

- if you just do greedy "rows only" you will not use rows 1,2,3,4
- if you just do greedy "cols only" you will not use cols 3,4,5,6,7,8

My construction produces the rectangles: 

- 1 1 5 1 (vertical up from point 5,1), 1 2 5 8 (the "big rectangle" that correctly fills the empty space), 
- 6 1 6 1 (the 1x1 with the point inside it on its own), and 6 2 6 8 (the horizontal rectangle line across from point 6,2)

Finally, note in solution below how the dummy value works to trigger "end of board processing": I noticed locally that my first solution was failing when there was only 1 point on board e.g.

R,C = 4,7 and point = 3,3

In the above personal test case, the rectangle was being produced as 1 1 3 7 rather than 1 1 4 7 due to faulty logic of the dummy value.

The dummy value should be **R+1**, so that when you are in the last "real row" it **always extends downwards to last board row, R via the check** `bottom_row = max(curr, below-1)`, which will be `max(curr, (R+1)-1)` when you reach the **dummy value** `below = R+1`.

## AC code

```python
from collections import defaultdict

R, C, num_points = map(int, input().split())

POINTS = defaultdict(list)
rows = set() # you don't need this actually, noticed after submission
for _ in range(num_points):
    r, c = map(int, input().split())
    rows.add(r)
    POINTS[r].append(c)

rows = sorted(rows)
# DUMMY VALUE R+1 triggers end of zip processing - see the step with bottom_row = max(curr, below-1)  
# the right element in the zip will be below==R+1-1 == R for the last zip pair
rows.append(R + 1)

top_row = 1
for curr, below in zip(rows, rows[1:]):
    bottom_row = max(curr, below - 1)
    cols = sorted(POINTS[curr])
    n = len(cols) # need to know how many points are in this row, as we need to treat the LAST POINT differently (see NOTES)
    left_border = 1
    for i, x in enumerate(cols, 1):
        if i != n:
            # current rectangle is top_row, bottom_row, left_border, x
            # there are still points to the right of this col, so do NOT extend to rightmost edge/border
            print(top_row, left_border, bottom_row, x)
            left_border = x + 1
        else:
            # this is the last point, so need to extend its rectangle to right border i.e. C
            print(top_row, left_border, bottom_row, C)
    top_row = bottom_row + 1

print(0) # this construction always works so always 0
```