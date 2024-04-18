# Diagonal Cut
# https://open.kattis.com/problems/diagonalcut
# TAGS: geometry, logic, proof, nice
# CP4: 5.3f, GCD and/or LCM
# NOTES:
"""
Nice little exercise:

A bit confusing/reading comprehension, since it says there are "blocks" and "grids" then also M*N "rectangles of identical shape and size"
BUT IT'S JUST 1x1 *SQUARES* ??? So it seems that the actual question, formulated clearly is: 
Q: "Given an MxN grid of 1x1 squares, how many 1x1 squares are cut exactly in half by a line from 0,0 to M,N" (WLOG, the other diagonal is same answer)

---

So, solving this above reformulation/interpretation: 
-> The repeating unit is a mini rectangle of sides m//gcd(m,n) and n//gcd(m,n)
-> If there is a 1x1 square in the mini rectangle which is divided exactly in half, it is a "central square" (by symmetry) such that 
   the diagonal goes through its centre. Such a square exists iif the mini rectangle has both its sides of odd integer length
   [draw a 1x3 or a 3x7 rect with the 2 axes of symmetry to visualize this]
-> Then the large m*n rectangle is made up of m//gcd * n//gcd mini rectangles of which the sqrt(qty) lie on the diagonal
   e.g. if 9*15 the mini rectangles are of dimension 3*5, and there are qty = 9 = 3**2 of them forming the large rectangle.
   Of the 9, only sqrt(9)=3 lie on the diagonal, and each contains exactly 1 square with a desired centrally symmetric point.

g = gcd(m,n)

mini_rect_side1 = m//g
mini_rect_side2 = n//g

how_many_mini_rects = m//mini_rect_side1 * n//mini_rect_side2

how_many_on_rects_on_diagonal = how_many_mini_rects**0.5

 ^^^ but simplifying above this is just ^^^  (m//g//m * n//g//n => g**2)**0.5 = g

So anwer is gcd(m,n) if both side lengths of the mini rectangle are odd, else 0.
"""
from math import gcd

m, n = map(int, input().split())

g = gcd(m, n)

res = g if (m // g % 2 == 1 and n // g % 2 == 1) else 0

print(res)