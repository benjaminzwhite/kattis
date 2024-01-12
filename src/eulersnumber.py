# Euler's Number
# https://open.kattis.com/problems/eulersnumber
# TAGS: mathematics
# CP4: 5.3g, Factorial
# NOTES:
"""
In Python you can compute the factorials easily, but will get TLE if you try up to n = 10_000

However, for large values of n, you can just stop at some max_value of n beyond which the result
no longer changes to within 1e-12 and use that instead of the full value of n

In practice max_value = 100 works for example.
"""
from math import factorial

n = int(input())

# if n is huge, don't compute up to factorial(n) -> just need terms up to e.g. factorial(100)
n = min(n, 100)

res = sum(1 / factorial(x) for x in range(n+1))

print(res)