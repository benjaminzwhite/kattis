# Detailed solution for Kattis - Sums / consecutivesums

[Problem statement on Kattis](https://open.kattis.com/problems/consecutivesums)

A nice clear problem statement: try to express `N` as the sum of consecutive integers, using the fewest number of terms.

## Tags

mathematics, number theory

## Solution

You want to express `N` as an arithmetic progression `N = a + (a+1) + (a+2) + (a+3) + ... + (a+b-1)` for some value of `a` and `b`.

If we say that the last term is `a+b-1` then the number of terms will be equal to `b`.

By the usual Gauss sum of arithmetic progression formula, this means that `N  =  b * (a + (a+b-1)) // 2 = b * (2*a+b-1) // 2`.

So you need to trial factorize `2 * N` and you are looking to see if `2 * N` can be expressed as `2 * N = b * Q` where `Q = (2*a+b-1)`.

You still have some "parity matching conditions" to consider though:

If you find any `b` such that `b` divides `2*N` i.e. `2*N % b == 0`, then you now need to check compatibility with `Q` being of the form `Q = (2*a+b-1)`.

1. Compute the quotient `Q = 2*N // b`. If this is **odd** then we have `Q = (2*a+b-1)` must be **odd** also. Since `2*a` is even, `2*a-1` is odd, so this means that the remaining component, `+b`, must be **even** to match the overall parity of `Q`.
2. Vice versa, if `Q = 2*N // b` is **even** then we have that `Q = (2*a+b-1)` must be **even** also. Since `2*a` is even, this means we want `b-1` to be **even**, i.e. we want `b` itself to be **odd**.

So for each candidate value of `b`, you need to check that the corresponding case for `Q` being even/odd is satisfied, if so then the value of `b` is OK. If you try all possible values of `b` in **ascending order** then of course the first valid value of `b` that you find will be the **smallest** valid value which is what the problem is asking for (i.e. corresponds to the solution for `N` using the fewest number of consecutive terms).

(Note therefore that the reasoning above implies that all integers `N` can be expressed as the sum of consecutive integers in at least one way, except when `N` is a perfect power of `2`)


### Implementation note

For performance requirements aspect of the problem (we are told that `N_max = 10**9)`: note that `2 * N = b * Q` where `Q` is a number greater than or equal to `b-1`. So `2 * N >= b * (b - 1)`, which means that we only need to check roughly `sqrt(2*N)` possible values for `b`.

See the `while b * b <= 2 * N` condition in the code below for this optimisation - this is what allows you to avoid checking all values of `b` up to `N = 10**9` which would timeout TLE.

## AC code

```python
T = int(input())

for _ in range(T):
    N = int(input())
    # N  =  a + (a+1) + (a+2) + (a+3) + ... + (a+b-1) = b * (a + (a+b-1)) // 2  = b * (2*a + b - 1)//2
    # so we try to look for:
    # 2*N = b * Q where Q = (2*a + b - 1)
    flg = True
    b = 2 # problem statement says need at least b=2 terms for expression to be valid (otherwise solution is trivial N = N, 1 term)
    while b * b <= 2 * N:
        if (2 * N) % b == 0:
            Q = (2 * N) // b
            # we have found b candidate - need to check the parity matching conditions (SEE NOTES ABOVE)
            if (Q % 2 == 1 and b % 2 == 0) or (Q % 2 == 0 and b % 2 == 1):
                a = (Q + 1 - b) // 2 # given the Q value above, solve for a to find the initial term of the arithmetic progression
                print(N, "=", ' + '.join(map(str, range(a, a + b)))) # print up to a+b-1 INCLUSIVE, so range up to a+b EXCLUSIVE
                flg = False
                break
        b += 1

    if flg:
        print("IMPOSSIBLE") # this should only print IMPOSSIBLE if N is a power of 2: {1,2,4,8,....}
```