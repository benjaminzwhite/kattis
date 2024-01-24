# Soylent
# https://open.kattis.com/problems/soylent
# TAGS: basic
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
from math import ceil

T = int(input())

for _ in range(T):
	N = int(input())

	print(ceil(N / 400))