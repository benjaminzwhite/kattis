# Varied Amusements
# https://open.kattis.com/problems/variedamusements
# TAGS: recurrence
# CP4: 0, Not In List Yet
# NOTES:
"""
- Found on PDF p126 of Sannemo - Principles of Algorithmic Problem Solving, multidimensional recursion paragraph/section.
- 2 Scoring groups; First: easy recursive for 1 point. Second: need to implement the iterative solution.
- I Included below the recursive solution I made for checking my iterative solution:

---

EXPLANATION:
Strings of length n using a given max number of chars from {a,b,c} such that no 2 consect letters appear.

Let A(x) be number of sequences of len x that DO NOT END IN a, same for B(x) and b, and C(x) and c.
Then:

A(x) = B(x-1) * b + C(x-1) * c  

since we build A(x) by taking a B(x-1) and adding {b} to it, or a C(x-1) and adding a {c} to it.
Similar reasoning for B(x) and C(x). So our result is:

R(n) = a * A(n-1) + b * B(n-1) + c * C(n-1)

---

# Recursive solution based on above explanation:

from functools import lru_cache

@lru_cache
def A(n):
	if n == 0: return 1
	return b*B(n-1) + c*C(n-1)

@lru_cache
def B(n):
	if n==0: return 1
	return a*A(n-1) + c*C(n-1)

@lru_cache
def C(n):
	if n==0: return 1
	return a*A(n-1) + b*B(n-1)

# Sample inputs given with a = 1, b = 2, c = 3 and n = 5
n, a, b, c = 5, 1, 2, 3 # expected answer is 1188 

res = a*A(n-1) + b*B(n-1) + c*C(n-1)

print(res)

"""
# Iterative solution for Full Scoring Group 2 points
n, a, b, c = map(int, input().split())

BIGMOD = 10**9 + 7

A, B, C = 1, 1, 1

for _ in range(n-1):
    # to n-1 since we want R(n) = a*A(n-1) + b*B(n-1) + c*C(n-1)
    A, B, C = b*B+c*C, a*A+c*C, a*A+b*B
    
res = a*A + b*B + c*C

print(res % BIGMOD) # can just do mod at the end because Python bigint O_o