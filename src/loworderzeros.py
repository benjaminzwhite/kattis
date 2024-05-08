# Low Order Zeros
# https://open.kattis.com/problems/loworderzeros
# TAGS: mathematics, number theory
# CP4: 5.3g, Factorial
# NOTES:
"""
Have solved before on other OJ's it's a classic exercise:

Lots of material online for this, search "last non zero digit of n factorial" etc.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def last_digit_factorial(n):
    LOOKUP = [1, 1, 2, 6, 4, 2]
    if n < 5:
        return LOOKUP[n]
    
    q, r = divmod(n, 5)

    return last_digit_power_of_two(q) * last_digit_factorial(q) * last_digit_factorial(r) 

@lru_cache(maxsize=None)
def last_digit_power_of_two(exp):
    # last digit of number of the form 2**exp
    if exp == 0:
        return 1
    else:
        return [2, 4, 8, 6][exp % 4 - 1]

while (n := int(input())):
    print(last_digit_factorial(n) % 10)