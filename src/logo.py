# Logo
# https://open.kattis.com/problems/logo
# TAGS: geometry, interpreter
# CP4: 7.2a, Points
# NOTES:
"""
Used cmath import for practice
"""
from cmath import rect, pi

T = int(input())

for _ in range(T):
    n = int(input())
    r, phi = 0, 0
    curr = rect(r, phi)

    for _ in range(n):
        op, val = input().split()
        val = int(val)
        if op == "fd":
            curr += rect(val, phi)
        elif op == "bk":
            curr -= rect(val, phi)
        elif op == "lt":
            phi += 2 * pi * (val / 360)
        else:
            phi -= 2 * pi * (val / 360)
    
    print(round(abs(curr)))