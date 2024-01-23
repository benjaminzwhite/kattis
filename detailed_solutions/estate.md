# Detailed solution for Kattis - Integer Estate Agent

[Problem statement on Kattis](https://open.kattis.com/problems/estate)

A really nice mathematics related exercise - but actually when solving it also feels a bit like an array-processing problem, where you are shifting values around.

**Comment:** I don't think that the "setting" of the problem adds much (it is talking about polygons etc.) - personally I would have just asked the question quite simply:

**"In how many ways can `N` be written as a sum of consecutive integers, STARTING FROM 2 (for some reason O_o)"**

## Tags

mathematics, number theory, array

## Solution

So with the restatement of the problem as given above, and with `N = 18` for example, we have: 

`N = 18` can be written as: `18, 5+6+7, 3+4+5+6` i.e. in `res = 3` different ways as a sum of consecutive integers.

Also, since we aren't allowed to use the value `1`, we have that e.g. `N = 10` can be written only as `10` so `res = 1` **since the solution `1+2+3+4` is not allowed as it uses a `1` in the sum.**

Observation:

For a given length of the possible candidate sequences (1 term, 2 terms, 3 terms ...) then **at most one sequence of that length** can possibly sum to `N`.

For example, for `N = 18`, `5+6+7` is the **ONLY** length-3 sequence; there cannot be any other (because if the first number is smaller than `5`, all the numbers are smaller than their counterparts in `5+6+7`, so the new sequence is strictly less than `5+6+7=18`, so the sequence doesnt work. Same argument for if the first number is greater than `5`, the new sequence would be strictly greater than `18`).

**This observation unlocks the idea for solving:** when you draw it, or think algorithmically about shifting all elements by `-1` or `+1` for example, you see clearly that e.g. considering the sequence `4+5+6 = 15` compared to `5+6+7 = 18` that **the resulting sum of the -1 shifted sequence is `-1 * 3` i.e. `-1 * NUM_TERMS` relative to the original sequence.**

By the same reasoning, e.g. why is there only one length 4 sequence: starting from `3+4+5+6 = 18`, you see that the "bad length 4 sequences" would be: 

```
Considering negative/decreasing shift amounts:

2+3+4+5 = 14 which is 18 + (-1 * 4) i.e. 18 + (negative 1 shift * num_terms)
1+2+3+4 = 10 which is 18 + (-2 * 4) i.e. 18 + (negative 2 shift * num_terms)

Or considering the positive/increasing shifting would be

4+5+6+7 = 22 which is 18 + (+1 * 4) i.e. 18 + (positive 1 shift * num_terms)
...
10+11+12+13 = 46 which is 18 + (+7 * 4) i.e. 18 + (positive 7 shift * num_terms)

```

While writing this out, you should realise that the exact same reasoning works "in reverse": the only sums involving `k` terms must be some multiple of `k` added to a **"fundamental starting sum"**. This fundamental starting sum is arbitrary, but WLOG you can take the smallest value, so that `k` is always positive: `+k, +2k, +3k...`) etc:

```
k=num_terms   "fundamental/representative sequence"     sequence shifted by +1,+2,+3 positions (NOTE HOW SUM IS +1,+2,+3 * num_terms)
 1                2                                       3,4,5,6,7...
 2                2+3 = 5                                 3+4 = 7 = 5 + 1*2, 4+5 = 9 = 5 + 2*2, 5+6 = 11 = 5 + 3*2 ...
 3                2+3+4 = 9                               3+4+5 = 12 = 9 + 1*3, 4+5+6 = 15 = 9 + 2*3, 5+6+7 = 18 = 9 + 3*3....
 4                2+3+4+5 = 14                            3+4+5+6 = 18 = 14 + 1*4, etc. etc.
```

So finally:

1. If you precompute the "fundamental sequences" above i.e. accumulate `2,3,4,...` until `N_MAX = 1_000_000`
2. Then, for each query `N`: 
   - If `N` can be expressed as a `k=2` term sequence, by the above argument, it must be able to be written as `N = FUNDAMENTAL(2) + x*2` for some `x`
   - If `N` can be expressed as a `k=3` term sequence, it is of the form `N = FUNDAMENTAL(3) + y*3` for some `y`
   - etc. etc.
3. And so now with this precomputation done, we just need to compute `( N - FUNDAMENTAL(k) ) % k` and check if this `== 0` !

### Implementation notes

To avoid 1-based indexing nightmare, you really want each of the accumulates to be indexed by the actual `k`.

So you want your precomputed `FUNDAMENTALS` to be `[0, 2, 5, 9, 14]` so that e.g. `FUNDAMENTALS[4] == 14` i.e. the representative `k=4` term sequence sums to `14 = 2+3+4+5`.

To do this, just use `0` as a dummy value in `0` index; this allows you to start the accumulate cleanly.

Also, here is a brute force for checking answers (for small `N` of course):

```python
def brute_force_solve(n):
    xs = list(range(2,n+1))
    cnt = 0
    for l in range(len(xs)):
        for r in range(l, len(xs)):
            if sum(xs[l:r+1]) == n:
                cnt += 1
    return cnt

print(brute_force_solve(n))
```

## AC code

```python
# -- Precompute the accumulate of 2,3,4,... = 2,5,9,14 --
# CARE! use dummy 0 index value, due to 1-based indexing
N_MAX = 1_000_000
FUNDAMENTALS = [0] # 0 is DUMMY to allow indexing to match k count, see notes
curr = 2
while FUNDAMENTALS[-1] <= N_MAX:
    FUNDAMENTALS.append(FUNDAMENTALS[-1] + curr)
    curr += 1

while (n := int(input())):
    cnt = 0
    k = 1
    while (x := n - FUNDAMENTALS[k]) >= 0:
        cnt += (x % k == 0)
        k += 1

    print(cnt)
```