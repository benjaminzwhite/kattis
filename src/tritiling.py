# Tri Tiling
# https://open.kattis.com/problems/tritiling
# TAGS: recurrence, mathematics
# CP4: 5.4e, Others, Harder
# NOTES:
"""
- Called "3 x n dominoes" in Sannemo book p128 PDF (maybe out of date/older site name)
- Sanity check: answer should be 0 for all odd values of n
- F(0) = 1 is initial condition (the "empty tiling")
- You can precompute all answers up to n=30 if you want.

---

Included here are 3 different approaches - you can use these as a "Rosetta stone" between
recursive and iterative approaches. The 3rd approach uses numpy for matrix multiplication, so can't
use on Kattis (since numpy import not allowed), but you can make your own pure-Python implementation
of matrix multiplication.

Below code doesn't include reading in inputs, just for testing locally.

Correct answer for n = 8 -> 153
Correct answer for n = 12 -> 2131

n_test = 8
# n_test = 12

---
# 1 - Recursive solution

from functools import lru_cache

@lru_cache
def F(n):
	if n == 0:
		return 1
	if n == 1:
		return 0
	return F(n-2) + 2 * G(n-1)

@lru_cache
def G(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return F(n-1) + G(n-2)

print(F(n_test))

---

# 2 - Implementing the bottom up iterative approach

def iter_tile(n):
	f1, f0, g1, g0 = 0, 1, 1, 0

	for _ in range(n):
		f1, f0, g1, g0 = f0 + 2*g1, f1, f1 + g0, g1

	return f0

print(iter_tile(n_test))

---

# 3 - Matrix multiplication approach

import numpy as np

def fast_matrix_power(mtrx, exp):
	r, c = np.shape(mtrx)
	assert r == c, "Input matrix is not a NxN square matrix"

	I = np.identity(r, dtype=object)

	while exp > 0:
		if exp % 2 == 1:
			I = I @ mtrx
		mtrx = mtrx @ mtrx
		exp //= 2

	return I

def tile_using_matrix_expon(n):
	init_conds = np.array([0,1,1,0])

	mtrx = np.array([
					[0,1,2,0],
					[1,0,0,0],
					[1,0,0,1],
					[0,0,1,0]])

	m = fast_matrix_power(mtrx, n)

	res = m @ init_conds

	return res[1]

print(tile_using_matrix_expon(n_test))

"""
def iter_tile(n):
	f1, f0, g1, g0 = 0, 1, 1, 0

	for _ in range(n):
		f1, f0, g1, g0 = f0 + 2*g1, f1, f1 + g0, g1

	return f0


while True:
	n = int(input())
	if n == -1:
		break

	res = iter_tile(n)

	print(res)