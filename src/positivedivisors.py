# Positive Divisors
# https://open.kattis.com/problems/positivedivisors
# TAGS: brute force, mathematics, number theory, improve
# CP4: 5.3k, Divisibility Test
# NOTES:
"""
TODO: IMPROVE: find a better (faster) approach, currently it's just brute force
"""
n = int(input())

res = []
for d in range(1, int(n**0.5) + 1):
    if n % d == 0:
        res.append(d)
        if d * d != n:
            res.append(n // d)

res = sorted(res)
for x in res:
	print(x)