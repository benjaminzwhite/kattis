# Soundex
# https://open.kattis.com/problems/soundex
# TAGS: dict, array
# CP4: 2.3b, DAT, ASCII
# NOTES:
import sys
from itertools import groupby

D = {"B":1, "F":1, "P":1, "V":1,
     "C":2, "G":2, "J":2, "K":2, "Q":2, "S":2, "X":2, "Z":2,
     "D":3, "T":3,
     "L":4,
     "M":5, "N":5,
     "R":6}
     
for line in sys.stdin:
    xform = ''.join(map(str, (D.get(c, ' ') for c in line)))
    res = ''.join(k for k, g in groupby(xform) if k != ' ')
    print(res)