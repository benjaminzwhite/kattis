# Sticky Keys
# https://open.kattis.com/problems/stickykeys/
# TAGS: basic
# CP4: 1.4g, 1D Array, Easier
# NOTES:
from itertools import groupby

s = input()

res = ''.join(k for k, _ in groupby(s))

print(res)