# Pseudoprime numbers
# https://open.kattis.com/problems/pseudoprime
# TAGS: mathematics, number theory
# CP4: 5.3b, (Prob) Prime Testing
# NOTES:
"""
Don't need any performance for the primality testing, so a bit
overranked in Python with mod power built-in O_o (it's an old exercise though)
"""
import sys

def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5) + 1))

for l in sys.stdin:
    p, a = map(int, l.split())
    if p == 0 and a == 0:
        break
    if pow(a, p, p) == a and not is_prime(p):
        print("yes")
    else:
        print("no")