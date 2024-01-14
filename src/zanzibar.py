# Stand on Zanzibar
# https://open.kattis.com/problems/zanzibar
# TAGS: basic, array
# CP4: 1.4e, Control Flow
# NOTES:
"""
For code golf you can note that the code below is basically summing max(snd - 2 * fst, 0)
over the pairwise (fst, snd) values in the input array
"""
T = int(input())

for _ in range(T):
	res = 0
	fst = float('inf')
	for snd in map(int, input().split()):
		if snd > 2 * fst:
			res += snd - 2 * fst
		fst = snd
	print(res)