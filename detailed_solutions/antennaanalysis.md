# Detailed solution for Kattis - Antenna Analysis

[Problem statement on Kattis](https://open.kattis.com/problems/antennaanalysis)

A variant on the "best time to buy/sell stock cooldown" type thought process.

## Tags

array, dynamic programming

## Solution

As always, think of an extreme test case to illuminate: how can you "know" about `x = 1000` option in this situation?

```
 i =    0   1  2  3  4
xs = 1000, 13, 5, 6, 2
```

Let `C = 10` for example.

When you are at `i=4` and looking behind:

- the contribution due to `delta_i` from `i=4` to `i=3` is the same as that from 3 to 2, 2 to 1 etc i.e. it is the constant, `C`.
- so this penalty is essentially linear in how far back you look, OR if you now think of the "penalty" as moving *forward* from each x
- so you can think of each `x`, at its original `i`, as **decaying in value** by `C` for each later index.

So in other words, you "can know about" the value `x=1000` at `i=0`:

If you are at `i=2` at "looking behind `delta_i = 2-0 = 2`" indices behind, your res will involve checking:

`delta_x = abs(5 - 1000) - C* abs(2)`

which **works out the same as propagating the `x=1000` value forward by 2 indices and "decaying" it by `C` each time**: i.e. compare "real `x = 5` at real `i = 2`" with "`decayed x' = 1000-C-C = 980` at "future" `i = 2`".

Note that, this means that at **each index there is only 1 possible optimal value of the "best available decayed `x` value"**:

For example imagine:

```
i  = 0    1     2
x  = 100  150   120   here propagating the i=0,x=100 value forward to i=1, it becomes decayed to 100-C = 90,
x' =  |_> 90          so IMMEDIATELY you can compare it to i=1 real value x=150 -> 150 > 90, so it will NEVER BE 
           |___>80    WORTH COMPARING THE 90 again
```

So to implement these ideas, track the current `max_possible_value`: at each `x`, the `max_possible_value` becomes:

- either `current_max - C`, since we moved +1 index so decayed by +1 unit of `C` compared to previous
- or `x` if `x` itself is big: it now becomes the new `curr_max` to propagate forwards and we can forget about all previous x's to the left.

Careful though: since it's the *absolute* difference, you need to handle the possibility that the best score is obtained w.r.t to "small" previous
`x` value (above I was using 1000 for emphasis as a "big" value): consider e.g.:

```
i  =  0     1     2 
x  = -100  -20    5
C = 3
```

Then comparing `5` with `-100` we see: `abs(5 - -100) - 2*C = 105-6 = 99`

Comparing `5` with `-20` we see: `abs(5- -20) - 1*C = 25-3 = 22`.

How do you implement the "update decaying x value" in this case? You **increment** by `C` as follows:

`i' = 1, x' = -100 + C = -97`

Since `-97` ends up being *smaller* than the "real value" `-20` at `i=1`, it will always be better to compare with this decayed value of `i=0`, `x=-100`
when looking behind and performing the `abs(x - prev_x)` calculation. Consistency check:

so now compare `i=2, x=5` with the "decayed" value of `i=0, x=-100`:

`abs(5 - -97) - 1*C = 102 - 3 = 99`, as before so all OK.

So at each `x`, you are updating `BIG_CANDIDATE` and `SMALL_CANDIDATE` as:

- `BIG_CANDIDATE = max(BIG_CANDIDATE - C, x)`
- `SMALL_CANDIDATE = min(SMALL_CANDIDATE + C, x)`

and at each `x`, the best possible result is the best i.e. MAX from these 2 candidates w.r.t to current `x`:

`res_at_x = max( abs(x - BIG_CANDIDATE),  abs(x - SMALL_CANDIDATE))`.

## AC code

```python
n, c = map(int, input().split())

xs = list(map(int, input().split()))

res = [0] # first x value always has score 0 since no previous elements (see testcase)

big, small = xs[0], xs[0] # start the lookbehind for both the "big" and "small" options with the initial values of i=0, x=xs[0]

for x in xs[1:]:
    big = max(big - c, x) # decay the big option, or take the curr x if even bigger
    small = min(small + c, x) # decay the small option, or take the curr x if even smaller
    tmp = max(abs(x - big), abs(x - small))
    res.append(tmp)

print(*res)
```