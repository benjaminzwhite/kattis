# Detailed solution for Kattis - Escape from Enemy Territory

[Problem statement on Kattis](https://open.kattis.com/problems/enemyterritory)

This is a nice exercise that combines a binary search with a BFS condition.

However there is (IMHO) a weird behavior/unexplained test case, which caused me to get WA on first submit:

Until I changed the limits of the binary search to have `low range == 0` I got WA. Before I had `low range == 1`: to me this makes sense, because the exercise is asking about "escaping" from enemy.

So, if I am not mistaken, this must mean there is a testcase in the exercise where the solution actually has the "minimum separation from an enemy base" being **0, in other words all their escape routes must at some point touch an enemy base?!** and this is the expected solution for such a testcase. I find this quite counterintuitive - if you passed through an enemy base on the way to the "escape endpoint", then surely you did not actually escape?

(I found this by making a testcase where there is an entire vertical wall of enemy bases separating start from endpoint, so you must cross it to reach the endpoint).


## Tags

binary search, BFS

## Solution

Basically the code below is solving in two steps:

1. Precompute `proximity` for each cell to nearest enemy base (BFS from each base to each grid cell and update with min distance to any base)
2. Then try a kind of "binary search BFS with min-allowed-proximity-to-any-base"

In other words, guess `mid`, then do a BFS and try to get from start to end coords, without at any point moving to a `(r, c)` which has `proximity < current_value_of_mid`.

If you **can** do this, then `mid` is ok, so binary search with **larger** `mid` (CARE! with the `lo/hi` confusion and shifting boundaries - you want to find the path that is as **far as possible** from any base so the "good outcome" from binary search is having `lo` **increase** to `mid`).

### Implementation notes

**My solution is a bit slower than 1-2 of the other Python 3 solutions, would like to improve speed when I have more experience: maybe my BFS implementation isn't good etc. One idea is that you can optimize the number of binary searches by setting `hi` to be the max distance encountered during processing, rather than always using `R*C`.**

Also, I use `(r, c)` i.e. "row" and "column" throughout, whereas inputs use `x, y` for the coordinates - **I always find this `x, y` variable names really error-prone when working with 2d grids, so there are a few parts in the input code where I am just swapping exercise's convention for my naming convention.**


## AC code

```python
from collections import deque

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# -- Inputs --
# CARE!: Exercise inputs uses x, y -> flip to get R, C in right place as my preference instead of y, x
B, C, R = map(int, input().split())
start_c, start_r, end_c, end_r = map(int, input().split()) # CARE! inputs as x,y so we want r,c so take them in as c,r

# Precompute the proximity information for the given input grid by doing BFS
proximity = [[None] * C for _ in range(R)]

bases = deque([])
for _ in range(B):
    bc, br = map(int, input().split()) # CARE! inputs as x,y so we want r,c so take them in as c,r
    bases.append((br, bc))
    proximity[br][bc] = 0

while bases:
    r, c = bases.popleft()
    for dr, dc in MOVES:
        if (0 <= (r_ := r + dr) < R) and (0 <= (c_ := c + dc) < C) and proximity[r_][c_] == None:
            proximity[r_][c_] = proximity[r][c] + 1
            bases.append((r_, c_))

# -- Binary search --
# UPDATE: see notes above about lo = 0 as starting condition for binary search (I had lo = 1 originally but it gives WA/RTE)
lo = 0
hi = R * C # TODO: for initial hi, can you just get the exact value of the highest distance from the bases precompute step earlier?
while lo < hi:
    mid = (lo + hi) // 2

    flg = False 
    
    if proximity[start_r][start_c] >= mid:
        q = deque([(start_r, start_c, 0)])
        seen = [[False] * C for _ in range(R)]
        while q:
            r, c, pathlen = q.popleft()
            if (r, c) == (end_r, end_c):
                flg = True
                res = [mid, pathlen]
                break
            if seen[r][c]:
                continue
            seen[r][c] = True

            for dr, dc in MOVES:
                if (0 <= (r_ := r + dr) < R) and (0 <= (c_ := c + dc) < C) and proximity[r_][c_] >= mid:
                    q.append((r_, c_, pathlen + 1))

    if flg: # CARE! think carefully about the binary search updating conditions here, see notes above.
        lo = mid + 1
    else:
        hi = mid

print(*res)
```