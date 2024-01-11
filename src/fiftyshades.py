# Fifty Shades of Pink
# https://open.kattis.com/problems/fiftyshades
# TAGS: basic
# CP4: 6.4a, String Matching
# NOTES:
N = int(input())

S=0
for _ in range(N):
	w = input()
	w = w.lower()
	if "rose" in w or "pink" in w:
		S += 1

if S == 0:
	print("I must watch Star Wars with my daughter")
else:
	print(S)