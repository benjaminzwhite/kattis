# Detailed solution for Kattis - Eko

[Problem statement on Kattis](https://open.kattis.com/problems/eko)

This is an exercise which "obviously" feels like a binary search task, but which can be solved analytically by thinking a little bit.

## Tags

array, sorting

## Solution

First sort the trees from tallest to shortest.

Moving from tallest tree to shortest, considering adjacent pairs of trees, if the gap between the **left** and the **right** tree multiplied by the total number of trees already counted to the left (call this value `cnt`), is <= amount of wood needed then you will need to have a saw height that is lower than this **right tree** in any case.

e.g. trees are `10 8 5 1` and lets say you need `12 units` of wood:

- from `10` to `8` you check and see that saw height of `8` will produce `(10-8) * 1 tree = 2` units of wood, so sum is now `sum = 2`
- from  `8` to `5` you check and see that saw height of `5` will produce `(8-5)  * 2 trees = 6` **EXTRA** units of wood, `sum = 2 + 6 = 8`
- from `5` to `1` you check and see that saw height of `1` will produce `(5-1) * 3 trees = 12` **EXTRA** units of wood, `sum = 8 + 12 = 20`

So the correct saw height is such that the sum is `> 8 units` but `< 20 units`, to reach the target `12` in this case:

At saw height `5` you can have `8` units, and this involves cutting `cnt = 3` trees (currently we are **just touching the roof** of 3rd tree, of height `5`, though)

So you are missing `12 - 8 = 4` units and are cutting `3` trees, so reducing saw height by `-1` would give you an extra `3 * 1 = 3` units, which is not greater than the `4` currently needed, so you need `-2` saw height to get `3 * 2 = 6` extra units to take you over the total of `12` needed (**note: in this case you therefore end with a total of `8 + 6 = 14 > 12` units of wood, i.e. you overshoot the exact target value of `12` but there is no better solution available**)


## AC code

```python
from math import ceil

N, needed = map(int, input().split())

xs = map(int, input().split())

xs = sorted(xs, reverse=True)
xs.append(-float("inf")) # dummy element to trigger processing of last real element in array

cnt = 0 # cnt number of "left" trees processed when iterating over left, right pairs (note: can do with enumerate(...) but this is clearer)
res = xs[0]
for l, r in zip(xs, xs[1:]):
    cnt += 1
    if (l - r) * cnt <= needed:
        needed -= (l - r) * cnt
        res = r
    else:
        res = l - ceil(needed / cnt) # reduce the height just enough so that leftover needed amount is taken care of
        break

print(res)
```

