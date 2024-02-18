# Temperature Confusion
# https://open.kattis.com/problems/temperatureconfusion
# TAGS: basic, mathematics
# CP4: 5.2i, Fractions
# NOTES:
from fractions import Fraction # yeah it's Python time O_o

n, d = map(int, input().split('/'))

F = Fraction(n, d)

C = (F - Fraction(32, 1)) * Fraction(5, 9)

print(C.numerator, '/', C.denominator, sep='')