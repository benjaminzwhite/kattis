# Exam Manipulation
# https://open.kattis.com/problems/exammanipulation
# TAGS: mathematics, combinatorics, brute force
# CP4: 3.2f, Iterative (Combination)
# NOTES:
from itertools import product

n, k = map(int, input().split())

students = []
for _ in range(n):
    students.append(input())

best = 0
for p in product(["T", "F"], repeat=k):
    tmp = min(
    	sum(curr == ref for curr, ref in zip(s, p))
    	for s in students
    	)
    best = max(best, tmp)

print(best)