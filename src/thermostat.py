# Thermostat Trouble
# https://open.kattis.com/problems/thermostat
# TAGS: mathematics, number theory
# CP4: 5.2i, Fractions
# NOTES:
"""
The question itself is simple, most of the code length is about formatting really.

You can use Fractions library but need to handle some specific requirements:
for example 0/anything should be output as 0/1 whereas Fraction will output 0
"""
from math import gcd

ts, qs = map(int, input().split())
temps = [None]
for _ in range(ts):
    o, c = map(int, input().split())
    temps.append((o, c))

for _ in range(qs):
    x, y, T = map(int, input().split())

    open1, close1 = temps[x]
    open2, close2 = temps[y]

    num = (T - open1) * (close2 - open2) + open2 * (close1 - open1)
    denom = close1 - open1

    G = gcd(num, denom)
    
    num //= G
    denom //= G

    if num == 0:
        denom = 1

    if denom < 0 and num > 0:
        denom *= -1
        num *= -1
    elif denom < 0 and num < 0:
        denom *= -1
        num *= -1

    print(f"{num}/{denom}")