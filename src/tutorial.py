# ICPC Tutorial
# https://open.kattis.com/problems/tutorial
# TAGS: mathematics
# CP4: 5.3g, Factorial
# NOTES:
"""
Basically you need to avoid calling factorial(10**9) and 2**(10**9) directly ofc O_o

You can simplify a lot of the ifs, just left for clarity

m_max = 10**9 implies that 12! <= m_max, and 13! > m_max
"""
from math import factorial, log2

m, n, t = map(int, input().split())

if t == 1:
    # m_max = 10**9: 12! <= m_max, 13! > m_max
    if n <= 12:
        res = (factorial(n) <= m)
    else:
        res = False
if t == 2:
    res = (n <= log2(m))
if t == 3:
    res = (n**4 <= m)
if t == 4:
    res = (n**3 <= m)
if t == 5:
    res = (n**2 <= m)
if t == 6:
    res = (n * log2(n) <= m)
if t == 7:
    res = (n <= m)

if res:
    print("AC")
else:
    print("TLE")