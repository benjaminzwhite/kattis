# Anagram Counting
# https://open.kattis.com/problems/anagramcounting
# TAGS: mathematics, combinatorics
# CP4: 5.4e, Others, Harder
# NOTES:
"""
- It's a multinomial counting exercise, don't need to optimize (at least in Python with big ints O_o)
- CARE! unknown number of input lines; I use try/except for these kind of problems to avoid I/O WA's.
"""
from math import factorial, prod

while True:
    try:
        s = input()

        numerator = factorial(len(s))
        denominator = prod(factorial(s.count(l)) for l in set(s))

        res = numerator // denominator

        print(res)
    
    except EOFError:
        break