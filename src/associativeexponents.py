# Associative Exponents
# https://open.kattis.com/problems/associativeexponents
# TAGS: mathematics, logic
# CP4: 0, Not In List Yet
# NOTES:
"""
If you take a = p1**e1 * p2**e2 etc. then taking (a**b)**c gives you res = p1 ** (b*c)*e1 etc for all prime factors
whereas a ** (b**c) gives you res' = p1 ** (b**c)*e1 for all prime factors

-> So the 2 results agree iif b*c == b**c

This happens for all b if c == 1 AND ALSO for b == c == 2 (isolated case). Otherwise, b**c is always > b*c.
CARE! Also case when a == 1 is always true 
"""
a, b, c = map(int, input().split())

if a == 1 or c == 1 or (b, c) == (2, 2):
    print("What an excellent example!")
else:
    print("Oh look, a squirrel!")