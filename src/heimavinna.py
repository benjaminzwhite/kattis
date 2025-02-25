# Homework
# https://open.kattis.com/problems/heimavinna
# TAGS: string
# CP4: 2.3c, DAT, Others
# NOTES:
"""
Can just always +=1 res for each term, and additionally += by right-left where applicable,
but below if/else layout is clearer.
"""
s = input()

res = 0

for term in s.split(';'):
	left, *maybe_right = term.split('-')

	if maybe_right:
		left = int(left)
		right = int(maybe_right[0])
		res += right - left + 1
	else:
		res += 1

print(res)