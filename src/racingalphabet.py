# Racing Around the Alphabet
# https://open.kattis.com/problems/racingalphabet
# TAGS: basic, geometry
# CP4: 7.2f, Quadrilaterals
# NOTES:
"""
- you have a speed of 15 feet per second, a DELTA between adjacent letters that is some weird float value
  hence the DELTA/15 to get number of seconds between chars
"""
from math import pi

ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \'"
DELTA = (2 * pi * 30) / 28

N = int(input())

for _ in range(N):
    s = input()

    res = sum(min(abs(ALPH.index(prev) - ALPH.index(curr)), 28 - abs(ALPH.index(prev) - ALPH.index(curr))) for prev, curr in zip(s, s[1:]))

    print(res * DELTA / 15 + len(s))