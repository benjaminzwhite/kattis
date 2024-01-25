# Sjecista
# https://open.kattis.com/problems/sjecista
# TAGS: mathematics, combinatorics, proof
# CP4: 9.form, Formulas/Theorems
# NOTES:
"""
- Each intersection point is uniquely determined by the intersection of 2 lines
- Each pair of 2 lines uniquely determines the diagonals of a quadrilateral, formed
  by 4 of the N vertices of the polygon
- So there are as many intersection points as there are distinct quadrilaterals that
  you can form on the N vertices of the polygon
- Since a quadrilateral is formed by choosing 4 out of the N vertices, our answer
  is just binomial(n, 4)

---

Note: Python's math.comb() handles the cases with n < 4 and returns 0 automatically
"""
from math import comb

n = int(input())

res = comb(n, 4)

print(res)