# Cokolada
# https://open.kattis.com/problems/cokolada
# TAGS: binary, mathematics, proof
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
"""
- The bar is always 1 x power_of_2 so e.g. 1x16, 1x32 etc

---

Imagine you want to make K = 6 squares, you have that exp = 3 i.e. 2**3 = 8 is the closest higher power of 2.

To get the K = 6 squares from here, you must divide 8 -> 4+4, then divide 4 -> 2+2 so you can form 6=4+2

Note in binary that K = 6 is = 110

So basically the "last step" will always be the one which produces the RIGHT MOST SET BIT of the target

e.g. from 8: 1000
to get to 6:  110
we must move s.e   <--- 2 jumps from (s)tart to (e)nd

e.g. from 16: 10000
to        10:  1010
we must move  s..e <--- 3 jumps from (s)tart to (e)nd

So find the rightmost set bit - you can use classic bit twiddling trick: K & ~(K-1)
then log2 to get how many positions along you need to move.
"""
from math import log2, ceil

K = int(input())

exp = ceil(log2(K))

rightmost_set_bit = K & ~(K-1)

lhs = 1 << exp

rhs = exp - log2(rightmost_set_bit)

print(int(lhs), int(rhs)) # CARE! cast to int to avoid printing decimals .0