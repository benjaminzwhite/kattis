# Detailed solution for Kattis - Divisibility Shortcut

[Problem statement on Kattis](https://open.kattis.com/problems/shortcut)

## Tags

mathematics, number theory, proof

## Solution

The key thing to understand/state clearly is that the "DS criterion" that is discussed in exercise **must hold for any arbitrary `n`.**

So, starting from **ANY** `n` in base `b` we write:

`n_b = c_1 * b**1 + c_2 * b**2 + c_3 * b**3 ....` where I'm writing in least significant digit to most significant L->R

and the sum of the digits of `n_b` is therefore:

`S = c_1 + c_2 + c_3 + ....`

So if we say that `S` is divisible by `d` we have `S = X * d` and we want this to imply `n` is divisible by `d` i.e. that `n_b = Y * d`, then we have:

`n_b - S = (Y-X) * d` i.e. this expression is divisible by `d` also.

Expanding and grouping terms:

`(c_1 * b**1 - c_1) + (c_2 * b**2 - c_2) + (c_3 * b**3 - c_3) + ...`

i.e. `c_1 * (b**1 - 1) + c_2 * (b**2 - 1) + c_3 * (b**3 - 1) + ...`

but the polynomials are all of the form:

`(b-1) * (1 + b + b**2 + b**3 + ...)`

So we have:

`(Y-X) * d = (b-1) * (c_1 * poly1 + c_2 * poly2 + c_3 * poly3 + .... )`

Now, **since we want this for ALL integers `n`** then the RHS expression containing the `poly1, poly2 ...` above will vary in general depending on the specific `n` (e.g if `b = 10` and `n = 11241` or `n = 531` the RHS will be different)

So we want `d` to divide `b-1` in general to ensure this equation holds for arbitrary `n`.

### Implementation note

There is just an extra requirement in the exercise: it wants the largest `d <= k` as the answer.

There are cleaner ways to implement the solution but code below follows the logic explained in the notes.


## AC code

```python
T = int(input())
for _ in range(T):
    b, k = map(int, input().split())

    bb = b - 1
    res = 1

    for d in range(1, int(bb**0.5) + 1):
        if bb % d == 0:
            q = bb // d

            # since d is increasing, bb//d is decreasing from max possible value so 
            # the FIRST q <= k you encounter, if any, is best possible answer
            if q <= k: 
                res = q
                break
            if d > k:
                break
            res = max(res, d)
    
    print(res)
```