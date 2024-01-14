# Reverse
# https://open.kattis.com/problems/ofugsnuid
# TAGS: basic
# CP4: 1.4g, 1D Array, Easier
# NOTES:
import sys

n = int(input())

res = [x for x in sys.stdin]

for x in res[::-1]:
    print(x)