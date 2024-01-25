# ACM Contest Scoring
# https://open.kattis.com/problems/acm
# TAGS: array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
from collections import defaultdict

solved = 0
time = 0
attempts = defaultdict(int)

while True:
	inps = input()
	if inps == "-1":
		break
	t, problem_id, right_or_wrong = inps.split()
	if right_or_wrong == "right":
		time += int(t) + 20 * attempts[problem_id]
		solved += 1
	attempts[problem_id] += 1

print(solved, time)