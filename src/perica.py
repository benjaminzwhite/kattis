# Perica
# https://open.kattis.com/problems/perica
# TAGS: mathematics, combinatorics
# CP4: 5.4b, Binomial Coefficients
# NOTES:
"""
For ex take n=5 and k=3 with xs = 8 7 6 5 4 (sorted in descending order)

The x=8 will appear as largest value in 876,875,874,865,864,854
The x=7 will appear as largest value in 765,764,754
The x=6 will appear as largest value in 654
The x=5,4 will not appear as largest

In other words:
- for the i=1,2,...K'th largest values, pick them in 1 way, 
- then pick (k-1) *SMALLER* values in comb(n-1-i, k-1) ways (n-1-i since they are the smaller values remaining)

-> the contribution to sum of the i'th largest value is therefore sorted_xs[i] * comb(n-1-i, k-1)
"""
from math import comb

BIGMOD = 10**9 + 7

n, k = map(int, input().split())
xs = sorted(map(int, input().split()))[::-1] # should use reverse=True instead O_o

res = sum(xs[i] * comb(n - 1 - i, k - 1) for i in range(n))

print(res % BIGMOD)