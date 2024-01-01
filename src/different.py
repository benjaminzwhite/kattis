# A Different Problem
# https://open.kattis.com/problems/different
# TAGS: basic
# CP4: 1.4b, Repetition Only
# NOTES:
import sys

for line in sys.stdin:
    inps = line.split()
    fst, snd = int(inps[0]), int(inps[1])
    print(abs(fst - snd))