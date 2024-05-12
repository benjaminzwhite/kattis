# Perfect Pth Powers
# https://open.kattis.com/problems/perfectpowers
# TAGS: mathematics, number theory
# CP4: 5.3h, Working with PFs
# NOTES:
"""
The hard part is the reading comprehension:
You have to notice that there is italic "magnitude" for value of x in the description so it seems that NEGATIVE integers are allowed

So if original n is negative you further factor out any factors of 2 from the final result since raising to any even power will 
change the parity of n

So for example if n is -343 then since |n| = 7**3, you can take 3 as the result for -343 also, since -343 = (-7)**3 <--has odd parity
However for e.g. -100 where |n| = 10**2, you CANNOT take 2 as the result since -100 != 100 = -10**2 <-- even parity

---

A concrete example where this leads to nontrivial result e.g. n = 3**6 * 5**6 = 11390625

With n > 0 then result is 6 since 15**6 = n

With n = -n then result is not 6 but "6_keep_dividing_by_2" => 3 since this allows you to take
( - (3*5)**2 ) ** 3 where here the exponents are |even part of 6|, |odd part of 6|
i.e. -225 ** 3 = -11390625 as required

Checked that this works also, e.g. with: -2**10 <-- 10 has odd part 5, -2**11 <-- 11 has odd part 11, -2**20 <-- 20 has odd part 5, etc
"""
from math import gcd
from functools import reduce

while True:
    n = int(input())
    if n == 0:
        break

    is_negative = False
    # update - need to handle negative n, see notes above
    # workaround - just take absolute value of n and flag if it was negative, handle later if so
    if n < 0:
        is_negative = True
        n = -n

    f = {}

    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            f[d] = exp
        d += 1

    if n > 1:
        if n not in f:
            f[n] = 0
        f[n] += 1

    res = reduce(lambda acc, x: gcd(acc, x), f.values())

    if is_negative:
        while res % 2 == 0:
            res //= 2

    print(res)