# Star Arrangements
# https://open.kattis.com/problems/stararrangements
# TAGS: basic
# CP4: 1.4e, Control Flow
# NOTES:
"""
3 cases:
- if n is evenly divisible by m, i.e. n % m == 0
- OR if n is evenly divisible by m + (m-1) (e.g. 6 stars then 5 rows repeating) , i.e. n % (2*m-1) == 0
- OR if n is divisible by m + (m-1) WITH m AS FINAL REMAINDER, i.e. n % (2*m-1) == m

(3rd case corresponds to e.g. 6,5,6,5,6 <--- where m=6 in final unmatched row)
"""
n = int(input())

print(f"{n}:")

for m in range(2, n):
	if (rem := n % (2 * m - 1)) == 0 or rem == m:
		print(f"{m},{m-1}")
	if n % m == 0:
		print(f"{m},{m}")