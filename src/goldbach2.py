# Goldbach's Conjecture
# https://open.kattis.com/problems/goldbach2
# TAGS: mathematics
# CP4: 5.3b, (Prob) Prime Testing
# NOTES:
"""
- Can brute force/compute all primes even in Python since N is small.
"""
N_MAX = 40_000
PRIMES = [False, False] + [True] * N_MAX
for i in range(2, int(N_MAX**0.5) + 1):
	if PRIMES[i]:
		for j in range(i * i, N_MAX, i):
	

T = int(input())

for _ in range(T):
	n = int(input())
	goldbach = []
	for i in range(n // 2 + 1):
		if PRIMES[i] and PRIMES[n - i]:
			goldbach.append(f"{i}+{n - i}")

	print(f"{n} has {len(goldbach)} representation(s)")
	for representation in goldbach:
		print(representation)
	print()