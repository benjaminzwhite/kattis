# Mean Words
# https://open.kattis.com/problems/meanwords
# TAGS: array, string
# CP4: 1.4g, 1D Array, Easier
# NOTES:
"""
Using '#' as fillvalue char: you can use anything that has isalpha() == False
"""
from itertools import zip_longest

n = int(input())

words = [input() for _ in range(n)]

res = []
for col in zip_longest(*words, fillvalue='#'):
	l, s = 0, 0
	for x in filter(lambda x: x.isalpha(), col):
		l += 1
		s += ord(x)
	res.append(chr(int(s / l)))

print(''.join(res))