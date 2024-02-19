# Fractional Lotion
# https://open.kattis.com/problems/fractionallotion
# TAGS: mathematics, number theory
# CP4: 5.2i, Fractions
# NOTES:
"""
1) we want x,y such that 1/x + 1/y = 1/n for some fixed n
2) x and y are > n (else if any <= n we would have e.g. 1/x >= 1/n and since 1/y is nonzero 1/x + 1/y > 1/n)
3) to avoid double counting, assume WLOG x >= y in the pair (x,y)
4) therefore x >= y > n and x,y,n integers
5) by 4) we can put x = n + a for some integer a
6) 1/(n+a) + 1/y = 1/n -> y = n**2/a + n
7) Solving 6) for a such that y is integer means finding an a that integer divides n**2 -> n**2/a = b
8) Then 7) gives the solution y = b + n, x = a + n.
9) To ensure that x >= y (for the double counting) we want a>=b, so in step 7) we only count the divisors of n**2 once -> try a in range (1,2...,n-1,n) rather than up to n**2

---

Implementation note:

It seems like there is a performance test, i.e. not just 3-4 values of n per test case. So will precompute all answers to N_MAX.

We want the number of divisors of n**2 for n in range(1, 10_000+1)
factorization of n = p1**e1 * p2**e2 * p3**e3 etc
factorization of n**2 = p1**(2*e1) * p2**(2*e2) * ...

So there are (2*e1 + 1) * (2*e2 + 1) * (2*e3 + 1) ... divisors of n**2

Note that this DOUBLE COUNTS pairs (a,b) == (b,a) with a!=b and SINGLE COUNTS the pair (a,b) == (n,n)

-> So to get only ordererd pairs single counted (a,b) we add +1 to res, to mimic
double counting (n,n) twice, then divide by 2 so that all pairs are single counted 
"""
import sys

# -- Precompute --
N_MAX = 10_000
RES = [0]
for n in range(1, N_MAX + 1):
    R = 1
    d = 2
    while d * d <= n:
        e = 0
        while n % d == 0:
            e += 1
            n //= d
        R *= 2 * e + 1
        d += 1
    if n > 1: # leftover prime factor - e.g. if n was 2*2*2*89, n is now 89
        R *= 2 + 1
    RES.append((R + 1) // 2)

# -- Queries --
for line in sys.stdin:
    _, n = map(int, line.split('/'))
    print(RES[n])