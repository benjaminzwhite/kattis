# Sum Squared Digits Function
# https://open.kattis.com/problems/sumsquareddigits
# TAGS: mathematics
# CP4: 5.2d, Base Number Variants
# NOTES:
P = int(input())

for _ in range(P):
	K, base, n=map(int, input().split())
	res = 0
	while n:
		res += (n % base)**2
		n //= base
	print(K, res)