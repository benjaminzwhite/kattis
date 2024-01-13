# Detailed solution for Kattis - Distance

[Problem statement on Kattis](https://open.kattis.com/problems/distance)

This is one of my favorite exercises on Kattis so far - it's a really nice and creative twist on the classic Manhattan distance problems.

I solved it with a "array-based" intuition, but maybe there is a more geometric way to get the result?

## Tags

mathematics, geometry, array

## Solution

To start with, as with most problems involving Manhattan distance, you should convince yourself that you can process the `x` and `y` coordinates separately (they don't "interact" with each other). So in what follows, I will focus on the 1D case of an array of `x` coordinates.

Suppose your x coords are: `[1, 6, 8, 8, 57]` and note - this will be important - that I have used two points in our testcase both with the **same** `x` coordinate `8` (for example, we could have points `(8,10)` and `(8,-972)` whatever).

Important observation: to move from `x_left = 1` to `x_left = 8`, you first have to get to `x_left = 6`, so we can focus on pairwise intervals.

Reformulation: I find it helpful to think about the points "moving/taking a trip" to the other points, rather than thinking about a fixed measured distance.

Draw something like this:

```
        _
        _   _
        _   _   
      1 _ 6 _ 8 _ 57
```

where _ means "points on the left will have to make a trip to get here". The _ are therefore counting the **number** of trips that the points on the left will have to make as they travel to reach all the points to their right.

So if you see 4 stacked _ it means you will need to perform that journey 4 times. In the drawing above, what I am saying is that the point at `x = 1` will have to travel from `1 -> 6` exactly 4 times : once as it goes to `x=6` itself, then **twice** as it goes the the 2 points at `x = 8`, and then once more as it travels to `x = 57`.

Now the entire insight is to ask **how many points will have to perform each of the journeys represented by _ above**:

First, we have that going from `1` to `6` is a distance of `abs(6-1) = 5`.

**Q1: How many times will this distance enter the total sum?**. Answer: as many times are there are points "to the right of point `x=1`"; these points are `6, 8, 8, 57` so there are 4 of them (again note the repeated `8`, we are counting actual points).

**Q2: How many points will need to perform this journey?**. Answer: Only one point so far (the point `x=1`) will be travelling to these 4 points.

Now repeat this reasoning:

Second, we have that going from `6` to `8` is a distance of `abs(8-6) = 2`.

**Q1: How many times will this distance enter the total sum?**. Answer: as many times as there are points "to the right of point `x=6`"; these points are `8, 8, 57` so there are 3 of them.

**Q2: How many points will need to perform this journey?**. Answer: **IMPORTANT - NOW 2 POINTS WILL ADD THIS ADDITIONAL DISTANCE: point x=6 AND THE PREVIOUS point x=1 will ALSO need to travel.**

etc. etc. so you accumulate the number of points that need to keep travelling "rightwards", and take into account the distance they need to next point reached as well as the number of "times" they need to do it (i.e. how many points are to the right).


### Implementation notes

I used detailed variable names below for clarity and left comments where I had implementation mistake while debugging.

- sort the counter keys (i.e. set) so you know what the 'next' x value is in the pairwise iteration (xleft - xright).
- however, for the *actual number of points*, make sure you take the len(arr) since you need to know how many actual points you travel to.
- e.g. debug with `(1,1), (100,12), (100,55), (100,87)`; you perform the `x=1 -> 100` journey 3 times in the total sum, not just once.

## AC code

```python
from collections import Counter

def clever_sum_manhattan(arr):
    c = Counter(arr)
    xs = sorted(c.keys()) # CARE! IMPORTANT TO TAKE SET OF x VALUES/use keys() so you only count once the distinct possible x values

    res = 0
    num_points_to_the_right = len(arr) # CARE! This however is no longer the distinct x values, but rather the ACTUAL NUMBER OF POINTS
    acc_points_to_move_now = 0
    for xl, xr in zip(xs, xs[1:]):
        hm_points_at_xl = c[xl]
        acc_points_to_move_now += hm_points_at_xl
        num_points_to_the_right -= hm_points_at_xl
        next_distance_to_move = abs(xl - xr)
        # need to perform this move, with all current acc points, how many times? ans: as many times as there are points to the right
        res += acc_points_to_move_now * next_distance_to_move * num_points_to_the_right

    return res

N = int(input())

x_values = []
y_values = []
for _ in range(N):
    x,y = map(int, input().split())
    x_values.append(x)
    y_values.append(y)

res = clever_sum_manhattan(x_values) + clever_sum_manhattan(y_values)

print(res)
```