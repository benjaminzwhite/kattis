# Neighbourhood Watch
# https://open.kattis.com/problems/neighborhoodwatch
# TAGS: mathematics, combinatorics
# CP4: 5.2b, Finding Formula, Harder
# NOTES:
"""
Nice little exercise - basically combinatorics, condition on leftmost house (drawing helps here to avoid i=0/1 index errors etc):

Track how many houses you've passed since the last safe house, as you move to the right (all walks that reach or go past that a safe house are safe)

e.g. for given testcase with safe_houses {1, 4} and N = 5, we have: all_houses = {1,2,3,4,5}:

Since House 1 is safe, all 5 houses (INCLUDING ITSELF) that are to the right are part of a safe walk starting at House 1.

So there are 5 safe walks that start at house 1

For House 2, the earliest safe house is house 4. So walk 2,2 is NOT SAFE, 2,3 is NOT SAFE, but 2,4 IS SAFE and 2,5 IS SAFE

So for House 2, we would just += 1 the number of houses passed since last safe house and wait until we reach House 4 to
actually calculate the contribution to the total res.

(If you're confused, draw it with intervals and follow the variable names used in code below - hopefully should be clear)

---

Note - if you want to code golf, you can rearrange and find an alternative approach that is much shorter
"""
N, K = map(int, input().split())
safe_houses = set()

for _ in range(K):
    safe_houses.add(int(input()))

num_houses_passed_since_last_safe_house = 0
res = 0
for i in range(1, N+1):
	num_houses_passed_since_last_safe_house += 1
	num_houses_to_the_right = N - i + 1 # 1 based indexing 
	if i in safe_houses:
		res += num_houses_passed_since_last_safe_house * num_houses_to_the_right
		num_houses_passed_since_last_safe_house = 0 # reset count

print(res)