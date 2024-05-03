# Arithmetic
# https://open.kattis.com/problems/arithmetic
# TAGS: mathematics
# CP4: 5.2c, Base Number Conversion
# NOTES:
s = input()

o = int(s, 8)

h = hex(o)

print(h[2:].upper())