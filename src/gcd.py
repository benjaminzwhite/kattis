# GCD
# https://open.kattis.com/problems/gcd
# TAGS: basic
# CP4: 5.3f, GCD and/or LCM
# NOTES:
from math import gcd

a, b = map(int, input().split())

print(gcd(a, b))