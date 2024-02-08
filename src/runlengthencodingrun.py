# Run-Length Encoding, Run!
# https://open.kattis.com/problems/runlengthencodingrun
# TAGS: array
# CP4: 1.6k, Cipher, Easier
# NOTES:
from itertools import groupby

op, s = input().split()

if op == 'E':
	res = ''.join(k + str(len(list(g))) for k, g in groupby(s))
else:
	res = ''.join(s[i] * int(s[i + 1]) for i in range(0, len(s), 2))

print(res)