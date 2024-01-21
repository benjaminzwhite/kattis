# Crne
# https://open.kattis.com/problems/crne
# TAGS: mathematics, calculus, proof
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
"""
- each vertical line creates H+1 regions
- each horizontal line creates V+1 regions
- so V as close to H as possible creates max (V+1)(H+1)
(e.g. maximize expression of the form (N // 2) * (N - N//2))
"""
N = int(input())

if N == 1:
	print(2)
else:
	V = N // 2
	H = N - V
	print((V + 1) * (H + 1))