# Expected Earnings
# https://open.kattis.com/problems/expectedearnings
# TAGS: basic
# CP4: 5.5a, Probability, Easier
# NOTES:
n, k, p = map(float, input().split())

if p * n - k >= 0:
	print("spela inte!")
else:
	print("spela")