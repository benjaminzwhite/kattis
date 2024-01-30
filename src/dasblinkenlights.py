# Das Blinkenlights
# https://open.kattis.com/problems/dasblinkenlights
# TAGS: basic
# CP4: 5.3f, GCD and/or LCM
# NOTES:
"""
- no lcm in Kattis Python 3.8, use gcd instead
"""
from math import gcd

p, q, s = map(int, input().split())

if p * q // gcd(p, q) <= s:
    print("yes")
else:
    print("no")