# Sum Kind of Problem
# https://open.kattis.com/problems/sumkindofproblem
# TAGS: mathematics
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
T = int(input())

for _ in range(T):
	c, N = map(int, input().split())

	res = N * (N + 1) // 2

	print(c, res, N * N, 2 * res)