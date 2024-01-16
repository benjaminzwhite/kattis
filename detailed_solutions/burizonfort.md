# Detailed solution for Kattis - Burizon Fort

[Problem statement on Kattis](https://open.kattis.com/problems/burizonfort)

A nice little mathematics-themed puzzle: but you don't actually need much number theory knowledge, it's more of a logical reasoning problem.

## Tags

logic, mathematics, array

## Solution

I personally unlocked the observation/recursion needed to solve by saying this:

"For each divisor `D`, in increasing size, if you can reach all target sums from `1` up to `S` **WITHOUT** using `D`, then by using `D` you can make
all target sums from `D` to `S + D`."

This therefore allows you to visualize the requirement as a kind of "overlapping intervals" problem: the "unreachable" numbers occur when, for any divisor `D`, the current value of `S` (as defined above) is less than `D`, because if so there is a **gap of unreachable numbers** between the previous `1 -> S` interval and the new `D -> D+S` interval.

For example, suppose you've reached a point where you can make all target sums from `1` to `9` using only the divisors of `m` that are less than `7`. Now you try to extend the `1 -> S=9` interval with the next divisor `D=7`: you see that it's OK to extend the coverage because if you use `D` now you
can make:

```
S'=7 (using D itself and using NONE of the previous sub-sums)                    |   this is the "overlap" interval with prev_S = [1,9] 
S'=8 (using D itself and using whatever previous sub-sum produced sum of 1)      |-- that ensures you don't miss any target values
S'=9 (using D itself and using whatever previous sub-sum produced sum of 2)      |   NOTE: how the LOWEST POSSIBLE D allowed would be D=10 (NOT D=9)
S'=10 (using D itself and using whatever previous sub-sum produced sum of 3)      
..
S'=7+S (using D itself and using whatever previous sub-sum produced sum of S)
```

And in the above case, we would continue the reasoning with a new value of `S' = 7 + S` and with the next value of `D' = next divisor after D`.

On the other hand, if you can make all target sums from `1` to `9` with all previous small divisors, but now the next divisor is `D=123` then
you will now get the following gap of unreachable numbers:

```
S=7
S=8
S=9
-- GAP! --                                                              |_____ and here you see the "GAP/MISSING OVERLAP" 
S'= 123 (using D itself and using NONE of the previous sub-sums)        |      as you can not produce S=10,11,...121,122
S'= 124 (using D itself and using whatever previous sub-sum produced sum of 1)
```

So the `S` we have been referring to above is therefore the **ACCUMULATE** of the divisors in increasing order, and you check that each subsequent `D` is such that `curr_D <= prev_S + 1`. 

### Implementation notes

Read the `curr_D <= prev_S + 1` requirement carefully, there is a subtle off-by-one error pitfall: it is `prev_S + 1`, not `prev_S`, because if e.g. `curr_D = 27` and `prev_S = 26` you **CAN MAKE** `prev_S + 1` by taking `curr_D + 0`, but if `curr_D = 28`, you **CANNOT MAKE** `27`, since you can only do up to maximum `26` with `prev_S` somehow and can only start from minimum value of `28` with `curr_D`.

For example: for `m = 20 -> divisors = {1,2,4,5,10,20}` as you start the process you can make `1,2,3` using the divisors `1,2` but when you try to make `4` you don't use any of the previous divisors and just use the divisor `4` directly, corresponding to the `curr_D + 0 = prev_S + 1` case explained above, with `curr_D = 4, prev_S = 3` in this case.


## AC code

```python
T = int(input())

for _ in range(T):
    m = int(input())
    divisors = set()
    d = 1
    while d * d <= m:
        if m % d == 0:
            divisors.update({d, m//d})
        d += 1
    divisors = sorted(divisors)

    # using variable names from notes above
    ok = True
    prev_S = 0
    for curr_D in divisors:
        if curr_D <= prev_S + 1:
            prev_S += curr_D
        else:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")
```

