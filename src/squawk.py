# Squawk Virus
# https://open.kattis.com/problems/squawk
# TAGS: mathematics, combinatorics, improve
# CP4: 5.8a, Matrix Power
# NOTES:
"""
TODO: IMPROVE: read this article for more advanced ideas/exercises:

https://cp-algorithms.com/graph/fixed_length_paths.html

---
Build the adjacency matrix and take it to the correct power:
(t-1) with my implementation, not (t) due to how I implemented (CARE! compare with numpy matrix_power())

Then the number of paths of length L reachable from s are all found
individually in row B[s] of the resulting matrix power B= A**(t-1)
So take sum of row B[s] to get answer.
"""
n, m, s, t = map(int, input().split())

A = [[0] * n for _ in range(n)] # build the adjacency matrix so can calculate how many paths of length L etc

for _ in range(m):
    i, j = map(int, input().split())
    A[i][j] = 1
    A[j][i] = 1

def matrix_multiply(a, b):
	return [[sum(a[i][k] * b[k][j] for k in range(n)) for i in range(n)] for j in range(n)]

# CARE! make sure you *copy* A !!
B = A[:]

# CARE! HERE due to taking (t-1) times the power of B with original A - whereas in numpy linalg matrix_power
# it's just matrix_power(A, t) [i tested locally and noticed the off by 1 error between NumPy solution and this Python sol]
for _ in range(t - 1):
    B = matrix_multiply(B, A)

res = sum(B[s])

print(res if t > 0 else 0)