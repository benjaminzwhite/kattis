# Detailed solution for Kattis - Divisors

[Problem statement on Kattis](https://open.kattis.com/problems/divisors)

Nice number theory exercise; there's a lot of optimization you can do for the precomputing, if you want to make the solution much faster.

## Tags

mathematics, number theory

## Solution

First, note that there are 10000 queries, so you'll need to do some precomputing (in Python at least O_o) to avoid TLE.

So, precompute for all `n < 432` the factorisation of `n!`. Note that you can do this efficiently by reusing the factorization of previvous factorial, `n-1 !`, at each step.

Here I'm doing it with a dict as follows:

`n! = {2: exp2, 3: exp3, 5: exp5, ... for all primes in n!}`

Then for each query, to work out number of divisors of $`\binom{n}{k}`$ :

1. lookup the exponent of each prime in the factorization of `n!`
2. then substract for each prime, the exponents of that prime in `n-k!` **AND** `k!`
3. now, whatever is "leftover" is the number of times `p` appears in $`\binom{n}{k}`$

Finally, the number of divisors is product of `(exponent + 1)` over all primes dividing the number.

## AC code

```python
import sys
from collections import defaultdict

# -- PRECOMPUTE --
def is_prime(n):
    return all(n % d > 0 for d in range(2, int(n ** 0.5) + 1))

PRIMES = [x for x in range(2, 431 + 1) if is_prime(x)]

FACTORIAL_FACTORIZATIONS = {0: defaultdict(int)}

for n in range(1, 431 + 1):
    n_ = n
    d = FACTORIAL_FACTORIZATIONS[n - 1].copy() # you just need to update the factorization of n-1! with the primes present in n itself; dont need to redo n! from scratch
    for p in PRIMES:
        while n % p == 0:
            d[p] += 1
            n //= p
    if n > 1:
        d[n] += 1
    FACTORIAL_FACTORIZATIONS[n_] = d
# -- end precompute --

# -- QUERIES --
for l in sys.stdin:
    n, k = map(int, l.split())

    res = 1
    for p, exp in FACTORIAL_FACTORIZATIONS[n].items():
        tmp = exp # these are the factors in the numerator of comb(n,k)
        tmp -= FACTORIAL_FACTORIZATIONS[k].get(p, 0)  # these are the factors in the denominator of comb(n,k) due to k!
        tmp -= FACTORIAL_FACTORIZATIONS[n-k].get(p, 0) # these are the factors in the denominator of comb(n,k) due to (n-k)!
        res *= (tmp + 1)
    
    print(res)
```