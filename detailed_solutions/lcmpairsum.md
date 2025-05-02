# Detailed solution for Kattis - LCM Pair Sum

[Problem statement on Kattis](https://open.kattis.com/problems/lcmpairsum)

An interesting number theory exercise with a nice visualization in terms of lattice points.

## Tags

mathematics, number theory

## Solution

The definition is:

`f(n) = sigma{1 <= p <= q <= n} of (p + q) subject to condition that lcm(p, q) is == n`

Draw a `n x n` lattice, label `p` and `q` axis starting from `1` to `n`:

```
        =q
        |
        v              

        5 . . . . .
        4 . . . . .
        3 . . . . .
        2 . . . . . 
        1 . . . . .
          1 2 3 4 5 <= p
```

Now, summing over all points 1 <= p <= q <= n:

```
. . . . .
. . . .
. . .
. .
.
```

is the same as summing over all points 1 <= q <= p <= n (just a change of variables, or flip the points if you are thinking geometrically:

```
        .
      . .
    . . .
  . . . .
. . . . .
```

So if you let `S(n)` be the sum over **all the lattice points**, then it is given by:

```
S(n) = "upper_triangle" + "lower_triangle" - 1x diagonal_points
                                                ^^^^^^
                         since we have included the diagonal twice, once in each triangle, so remove ONCE by inclusion-exclusion


S(n) = f(n) + f(n) - sigma{p == q} of (p + q) subject to condition that lcm(p, q) is == n

      the only term in this ^^ summation is the term where p == q == n since e.g. if p == q== 1, or 2 or 3... their lcm is NOT == n
      so the sigma is: 0 + 0 + 0 + ... + (p==n + q==n) = 2*n
 
S(n) = 2 * f(n) - 2 * n
```

Now, if `n` is a prime number, `PRIME`, then:

```
S(PRIME) = sigma{all p, q} (p + q) subject to condition that lcm(p, q) is == PRIME
         =    (1 + PRIME) + (PRIME + 1) + (PRIME + PRIME)
              i.e. only 3 cases are: p==1, q==PRIME / p==PRIME,q==1 / p==q==PRIME are the only 3 lattice points where lcm(p,q) == PRIME)
         =  2 + 4 * PRIME
```

If we define `PRIME_POWER_exp = PRIME**exp` then:

```
(imagine for definiteness that n == 81 == 3**4 -> then the only values where lcm(x,n)==n are 1,3,9,27,81)

S(PRIME_POWER_exp) = sigma(all p,q) (p+q) subject to condition that lcm(p,q) is == PRIME**exp
                   = (1 + PRIME**exp) + (PRIME**exp + 1) + (PRIME + PRIME**exp) + (PRIME**exp + PRIME) + .... + (PRIME**[exp-1] + PRIME**exp) + (PRIME**exp + PRIME**[exp-1]) + (PRIME**exp + PRIME**exp)

                   CARE! NOTE QBOVE ONLY 1 COPY OF LAST TERM
                   
                   ---

                   The above, with the concrete case of n==81==3**4 is:
                   = (1 + 81) + (81 + 1) + (3+81) + (81+3) + (9+81) + (81+9) + (27+81) + (81+27) + (81 + 81)
                   CARE! NOTE THE LAST POINT (81+81) WITH p==q ONLY APPEARS "ONCE" THE OTHER p/q q/p APPEAR TWICE WITH p/q flipped                 
```

In the above example with `n == 81`, this corresponds to:

- `2` full copies of the progression `1+3+9+27+81` from exponent `p**0` to `p**4`
- `2 * exp` times the `81` that is paired with `1,1,3,3,9,9,27,27` that we have **not** included to make the 2 full copies of the progression

So the sum of the progression is: `(1 - PRIME**(exp + 1)) // (1 - PRIME)`, and therefore:

```
S(PRIME_POWER_exp) = 2*{full copies of progression}         +    2*exp * PRIME_POWER_exp
                   = 2*(1 - PRIME**(exp+1)) // (1 - PRIME)  +    2*exp * PRIME_POWER_exp
```

Finally, note that `S(n)` is multiplicative **but we need to be careful**, as we pick up an extra factor of `2 *` in `S(n) = 2 * f(n) - 2 * n` every time we obtain `S(h = n * m) = S(m) * S(n)` when doing multiplicative decomposition, so we will need to divide our `S(n)` at the end by some power of `2` that will depend on how many multiplicative terms we needed (to be more precise, this number of terms is **how many distinct prime factors there are**).

## AC code

```python
T = int(input())
for testcase in range(1, T + 1):
    C = int(input())
    # -- S(n) is multiplicative; init to 1 and multiply *=
    # -- n is product of its prime factors so init to 1 also
    S_n, n = 1, 1
    for _ in range(C):
        prime, exp = map(int, input().split())
        prime_power = prime ** exp
        n *= prime_power
        S_n *= 2 * (1 - prime ** (exp + 1)) // (1 - prime) + 2 * exp * prime_power # see notes

    # -- S(n) = 2*f(n) - 2*n = 2*(f(n) - n)
    # Since we have multiplied C times i.e. performed C multiplications to get S(n) from its multiplicative
    # components S(n) = S(p1**exp1 * p2**exp2 ...) etc
    # then we have picked up C EXTRA factors of 2, relative to S(n) = 2*f(n) - 2*n = 2*(f(n) - n), so remove those
    rescaled_S_n = S_n // 2 ** C
    # now f(n) = rescaled_S_n + n
    f_n = rescaled_S_n + n
    BIGMOD = 10**9 + 7 # I forgot this and noticed just before submitting - you should do %= during calculations but Python bigint works anyways
    print(f"Case {testcase}: {f_n % BIGMOD}")
```