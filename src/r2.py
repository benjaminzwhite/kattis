# R2
# https://open.kattis.com/problems/r2
# TAGS: basic
# CP4: 1.4a, I/O + Sequences Only
# NOTES:
import sys

for line in sys.stdin:
    inps = line.split()
    r1 = int(inps[0])
    s = int(inps[1])
    
    print(2*s - r1)