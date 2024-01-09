# Detailed solution for Kattis - Farey Sums

[Problem statement on Kattis](https://open.kattis.com/problems/fareysums)

A nice little observation involving [Farey sequence](https://en.wikipedia.org/wiki/Farey_sequence) properties.

## Tags

mathematics, number theory

## Solution

It helps to use a concrete example: focus on going from F_3 to F_4, suppose you know FareySum(3) already, how does the sum change going to FareySum(4) ?

```
F_3 =   0/1         1/3    1/2    2/3          1/1
F_4 =   0/1  *1/4*  1/3    1/2    2/3  *3/4*   1/1
```

you see that the newly appearing Farey fractions modify the sum as follows **in pairs**:

Previously we had a term `1/3` (due to `0/1 -> 1/3` denominators) and a **paired term** `3/1` (due to `2/3 -> 1/1` denominators)

By inserting `1/4` and `3/4` these terms no longer exist, instead we get 2 * 2 new terms, in pairs also:

`1/4 + 4/3` on the left side (due to `0/1 -> 1/4 -> 1/3`) and `3/4 + 4/1` on the right side (due to `2/3 -> 3/4 -> 1/1`)

In general, let's call the "paired terms" that get replaced: `n/d` and `d/n` (e.g above `n=1,d=3` and our terms are `1/3, 3/1`)

By the usual Farey rules (read wiki article if you need proof), **the intercalated new fraction between `a/b` and `c/d` is the median `p/q = a+c/b+d`**

You can for example check that `1/4` is between `<0/1, 1/3> = 0+1/(1+3) = 1/4`, ok.

Therefore, since we only care about the denominators, if the paired denominator terms are e.g. `n/d` and `d/n` then the **new** denominator sums are:

1. `n/(n+d) + (n+d)/d` on the left, and on the right: `d/(n+d) + (n+d)/n`

(With our concrete example, what im talking about here is e.g. `1/3 + 3/1` contribution from F_3 gets replaced by: `1/4+4/3  + 3/4+4/1`  in F_4)

Finally, simplifying Eq1 above, you see that **the new contribution** `1 + n/d + 1 + 1 +d/n = 3 + n/d + d/n` while **the old contribution** is `n/d + d/n`.

So removing old contribution from new, we find that every *pair* of new terms in the new Farey sequence **always** contributes exactly `+3` to the new sum!

### Implementation

So now it's just [Euler phi](https://en.wikipedia.org/wiki/Euler%27s_totient_function) and initial conditions:

The total FareySum for F_n is the FareySum for `F_(n-1) + (3 * the number of pairs added in F_n)`

and the number of **pairs** added in F_n is just `euler_phi(n) / 2` (where divide by 2 due to counting pairs of terms, not how many single terms)

The initial condition is that `F_1 : 0/1 1/1` has `FareySum = 1/1 = 1`

So the solution for any query can be precomputed by first accumulating `euler_phi(n) / 2` up to max query value, multiplied by 3, and remove 1 due to F_1 == 1 initial value.


## AC code

```python
from itertools import accumulate

def euler_phi(n):
    res = n
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            res -= res // p
    if n > 1:
        res -= res // n
    return res

# -- Precompute --
N_MAX = 10_010 # 10 is sentinel O_o
PHI = [euler_phi(x) for x in range(N_MAX)]
RES = list(accumulate(PHI))

# -- Queries --
P = int(input())
for _ in range(P):
    K, N = input().split()
    print(K, f"{3 * RES[int(N)] - 1}/2")
```
