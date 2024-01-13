# Detailed solution for Kattis - Factorial Power

[Problem statement on Kattis](https://open.kattis.com/problems/factorialpower)

A good number theory exercise - we are going to make use of [Legendre's formula](https://en.wikipedia.org/wiki/Legendre%27s_formula) which can be used to find the largest power of a prime `p` that divides `n!`.

## Tags

mathematics, number theory

## Solution

First we factorize `n` (see *Implementation note* below for why you should do this step first!)

Then do use Legendre formula on the primes that appear in $`n = p_{1}^{e_{1}} \times p_{2}^{e_{2}} \times p_{3}^{e_{3}} ...`$ - call these values the `legendre[p]` scores for each of the prime factors of `n`.

Then the result will be the smallest of all the ratios between exponents across the factors of `n`. An example will be clearer:

Suppose `n = 151263` which factorizes as `n = 3**2 * 7**5`, with prime factors `p1 = 3` and `p2 = 7`.

Now lookup `p1 = 3` and `p2 = 7` in the Legendre results for `m!`: if `Legendre(m, 3) = 1001` for example, then you could in principle raise `n**500` because here the exponent of `p1 = 3` would then become `2 * 500 = 1000` which is indeed `<= 1001` i.e. the Legendre score for `3`.

However, you also need to check `Legendre(m, 7)` - suppose it is `= 11`, i.e the max power of `p2 = 7` in `m!` is `7**11`.

Then this constrains `n**k` since now you **CANNOT** raise `n` to the earlier-found very large value of `500`, since it would lead to the `7**5` contribution also being raised to `**500` i.e. `7**5 ** 500 = 7**2500` which is greater than `11`, the actual exponent of `7` in `m!`.

So you are constrained by the smallest of these possible values; and the max you can raise `7**5` to is `**2` since `7**5 **2 = 7**10` and here `10 < 11`.

In other words, it is constrained by the floor of `(legendre[p] / exponent_of_p_in_n)` across all the primes appearing in the factorization of `n`.

### Implementation notes

A very important performance observation is as follows:

If you do the Legendre calculation on **all the primes** up to `10**7`, and then *afterwards* you do the prime factorization of `n` in order to compare the primes in `n` to the Legendre results, you will get TLE (in Python at least).

**But clearly you only need to do the Legendre calculation on the primes that actually appear in the factorization of `n`. So factorize n first, then do Legendre theorem on the primes that appear in n = p1**e1 * p2**e2 etc. This leads to much smaller number of required Legendre calculations to perform.**


## AC code

```python
from math import floor

n, m = map(int, input().split())

# CARE! store the original input for later, as we will modify n while getting its prime factorization
n_orig = n

# -- Get prime factorization of n --
factors = {}
d = 2
while d * d <= n:
    exponent = 0
    while n % d == 0:
        n //= d
        exponent += 1
    if exponent > 0:
        factors[d] = exponent
    d += 1
if n > 1:
    if n not in factors:
        factors[n] = 0
    factors[n] += 1

# -- Apply Legendre's formula to the known primes that appear in n (see Implementation note above) --
legendre = {}
for p in factors:
    exponent = 0
    k = 1
    while True:
        curr = floor(m / pow(p,k))
        if curr == 0:
            break
        exponent += curr
        k += 1
    legendre[p] = exponent

# -- The result is the min ratio between exponents across the factors of n --
largest_k = float('inf')
for prime, exponent in factors.items():
	largest_k = min(largest_k, floor(legendre[prime] / exponent))

print(largest_k)
```

