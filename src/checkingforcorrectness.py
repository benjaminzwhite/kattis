# Checking For Correctness
# https://open.kattis.com/problems/checkingforcorrectness
# TAGS: mathematics, interpreter
# CP4: 5.8a, Matrix Power
# NOTES:
"""
Easy with Python pow() with mod
"""
import sys

for l in sys.stdin:
    a, op, b = l.split()
    if op == '^':
        a = int(a)
        b = int(b)
        res = pow(a, b, 10000)
    else:
        res = eval(l) % 10000
    print(res)