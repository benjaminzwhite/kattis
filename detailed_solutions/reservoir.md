# Detailed solution for Kattis - Reservoir

[Problem statement on Kattis](https://open.kattis.com/problems/reservoir)

Nice variant of the "largest rectangle in a skyline" type coding problems.

## Tags

binary search, stack

## Solution

I solved the "individual" case quickly but I didn't notice that, while `N` is `10**5`, **the number of queries `Q` is also** `10**5` so you need to think about performance implementation.

My original approach was to compute the answer on a case by case basis for each query: in this approach, you init a `"total_water_quantity"` and you
decrement it by the amount of volume newly available as you move from barrier to barrier. Then, as soon as `total_water_quantity <= 0`, you stop: the previous barrier was the last one to overflow.

Now, to deal with `10**5` queries, I redesigned slightly:

I focus on the `"total_volume"` available in the system, as a function of which barrier you are at (**note:** this quantity is strictly increasing of course, **therefore already sorted for a binary search !**).

As before, I compute the "available volume" provided by each new barrier. However, now I accumulate this into a `total_vol` accumulator, which I then store in a `VOLS_AT_BARRIERS[]` list. I uppercase the variable name here just to emphasize that it's precomputed once.

- this list therefore says, e.g. "up until and including barrier 123, you can use a total_volume of 5892 units of water"

This allows for `10**5` queries because now you just then **binary search this precomputed** `VOLS_AT_BARRIERS[]` list: find the value which is >= the water quantity in the given query; this is the result asked for by the exercise.

### Implementation notes

I left a few large comments in code below at important points. Some additional Python magic/quality of life stuff:

If you use `bisect_left` it handles all the various cases nicely.

For example, when `waterquantity < total_vol` for 1st barrier, it returns 0 as expected.

Also for case where water quantity is huge i.e. > `VOLS_AT_BARRIERS[last_element]`: then `bisect_left` gives the `last index + 1`, which corresponds to the **number** of the last barrier, as expected for the exercise.

Also for case where water quantity == **exactly** a value within the `VOLS_AT_BARRIERS` e.g. `water_quantity = 13`, `VOLS_AT_BARRIERS = [2, 13, 16, 18]` (this is test case query #2 in fact): `bisect_left` returns `index = 1` which corresponds to the "right answer" i.e. **first barrier** overflows, but **second barrier** does not.

Note this is not very maintanable code because of +1/-1 index and numbering, huge confusion, but it works for competitive programming situation O_o.

**Also, really to re-emphasize a point made in notes above:** the `VOLS_AT_BARRIERS` list, since it is strictly increasing (you can only add positive amount of vol, for each next barrier) then **this list is already sorted so you can binary search it directly.**


## AC code

```python
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
```