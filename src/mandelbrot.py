# Mandelbrot
# https://open.kattis.com/problems/mandelbrot
# TAGS: mathematics, geometry
# CP4: 7.2a, Points
# NOTES:
import sys

case_number = 0

for l in sys.stdin:
    case_number += 1
    
    r, i, n = l.split()
    r = float(r)
    i = float(i)
    n = int(n)

    c = r + i * 1j
    z = 0

    flg = True
    for _ in range(n):
        z = z * z + c
        if abs(z) > 2:
            flg = False
            break

    if flg:
        print(f"Case {case_number}: IN")
    else:
        print(f"Case {case_number}: OUT")