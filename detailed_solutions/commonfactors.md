# Detailed solution for Kattis - Common Factors

[Problem statement on Kattis](https://open.kattis.com/problems/commonfactors)

A nice number theory exercise, where you need to do some logic/optimization to get an AC solution also.

## Tags

mathematics, number theory

## Solution

The idea is you want to find maximum value of `g(k) = f(k) / k` where `f(k)` counts how many numbers `<= k` share a factor with `k`.

So the answer depends on Euler totient function, and a bit of logic:

- the number which has the most sharable factors is the one with all primes i.e. `2*3*5*7`
- if you want this to be as small as possible, only use `exponent = 1`, i.e. `2*3*5*7` rather than `2**331 * 3**4774` etc since they produce **the same numerator for a given denominator**

So the answer is:

- `denominator` = "largest product of all primes such that product `<= target_n`"
- `numerator` = "how many numbers share a factor with `denominator`", which is `numerator - euler_phi(denominator)`

**But since `denominator` is of the form** `p1*p2*p3...` then `euler_phi()` will always be `(p1-1)*(p2-1)*(p3-1)...` **in other words you don't need to actually "calculate" it:** the `denominator` is always the product of the first `k` primes such that product `<= target_n` and then the `euler_phi()` of this number (which we need to calculate the `numerator`) is just product of `(prime-1)` for all these same `k` primes.

So just do some precomputing of prime numbers until you have all possible primes needed for the largest testcase, see code below.


## AC code

```python
from math import gcd

# -- Precompute --
N_MAX = 10**18
SIEVE_MAX = 54 # generates first 54 primes: this is so that product of all of them is > 10**18 for the first time
SIEVE = [True] * SIEVE_MAX
SIEVE[0] = False
SIEVE[1] = False
PRIMES = []
for d in range(2, SIEVE_MAX):
    if SIEVE[d]:
        PRIMES.append(d)
        SIEVE[d * d::d] = [False] * ((SIEVE_MAX - d * d - 1) // d + 1)

# -- Query --
target_n = int(input())

curr_prod = 1
euler_phi_acc = 1
for p in PRIMES:
    if curr_prod * p > target_n:
        break
    else:
        curr_prod *= p
        euler_phi_acc *= (p - 1)

res_numerator = curr_prod - euler_phi_acc

g = gcd(res_numerator, curr_prod)

print(f"{res_numerator // g}/{curr_prod // g}")
```