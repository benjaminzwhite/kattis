# Sort
# https://open.kattis.com/problems/sort
# TAGS: sorting
# CP4: 2.2g, Special Sorting
# NOTES:
"""
Python comment/easy bug to miss:

behavior of Counter: it SHOWS you the __repr__ as most_common/sorted but you need to access via .most_common() to get the order
otherwise k,v items() will be in the ORDER THEY WERE ADDED TO COUNTER
"""
from collections import Counter

N, C = map(int, input().split())

xs = input().split()

c = Counter(xs)

print(*(' '.join(k for _ in range(v)) for k, v in c.most_common()))