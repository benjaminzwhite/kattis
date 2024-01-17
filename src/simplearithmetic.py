# Simple Arithmetic
# https://open.kattis.com/problems/simplearithmetic
# TAGS: mathematics
# CP4: 2.2i, Big Integer
# NOTES:
"""
Can cheese it in Python with Decimal
"""
from decimal import Decimal

a, b, c = map(int, input().split())

print(Decimal(a) * Decimal(b) / Decimal(c))