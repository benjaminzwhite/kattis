# Divisor Shuffle
# https://open.kattis.com/problems/divisorshuffle
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
"""
Should be self-explanatory code: the only tricky part is you need to account for inputs like e.g.

1 2 4 1 2 4

-> the result is 4,4 not 2,4

(Don't forgot to put {b} as initial seen() set, if you put {} the result will be 2,4 !!! it wont use 4 twice)
"""
N = int(input())

xs = sorted(map(int, input().split()), reverse=True)

B = xs[0]
seen = {B}
for x in xs[1:]:
	# search for the next largest number that either: does not divide B, or is already in seen()
	# (this handles case like eg. 1 2 4 1 2 4; the 2nd occurence of 4 means that there are 2 copies of 4 that are both largest possible values in the list)
    if x in seen or B % x != 0:
        A = x
        break
    seen.add(x)

print(A, B)