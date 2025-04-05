# Fair Warning
# https://open.kattis.com/problems/fairwarning
# TAGS: mathematics, number theory
# CP4: 5.3f, GCD and/or LCM
# NOTES:
"""
It's 99% reading comprehension; they are trying to "disguise" the fact that you are supposed
to find the GCD of something, but end up writing 5 paragraphs of incomprehensible stuff
with false leads and confusing metaphors. Don't enjoy this style personally.

Anyway, the actual "solving" part:

You have a list of ints, xs = [10, 15, 333] etc.

Find the smallest delta such that all the values: (x+delta for x in xs) are divisible by the same "biggest possible T"

if x + delta = k*T
and  y + delta = l*T
then x+delta-y-delta = x-y = (k-l)*T i.e. x-y is divisible by T also

So find GCD of the *differences* between the ints - call this G.

Then the delta you are looking for is the smallest value such that x + delta (for any x will work of course) is a multiple of G

e.g. with testcase:

26000, 11000, 6000
GCD(^differences^) = 5000

take e.g. x = 26_000 -> divmod(26_000, 5000) => 5*5000 + 1000
=> so need to add (5000 - 1000) = 4000 to reach 30_000 which is next full multiple of 5000
[try with 11_000, or 6_000, result is same: 11_000 + 4000 is divis by 5000, 6_000+4000 is divis by 5000]

---

Implementation note:

In Kattis Python 3.8, you can't use multiple arguments with math.gcd so have to build it yourself O_o
"""
from functools import reduce
from math import gcd

T = int(input())
for testcase in range(1, T + 1):
    _, *xs = map(int, input().split())
    
    diffs = (abs(l - r) for l, r in zip(xs, xs[1:]))

    g = reduce(gcd, diffs)

    res = -xs[0] % g # can use any x value, see notes

    print(f"Case #{testcase}: {res}")