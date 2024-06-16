# Rice judge aka risdomare
# https://open.kattis.com/problems/risdomare
# TAGS: sorting
# CP4: 0, Not In List Yet
# NOTES:
"""
Implement custom sorting basically.

First sort on x[0] + x[1].
Then tiebreak on whether the input preference (I call this "kw" below) is "antal" or "storlek"

Tiebreak implementation (not very maintainable/good practice O_o):

Check either x[0] or x[1], with the index using Python bool behavior
depending on whether kw == "storlek" -> True -> 1, so look at x[1] etc.
"""
n = int(input())

kw = input()

xs = []
for i in range(1, n + 1):
    portion, grainsize = map(int, input().split())
    xs.append((portion, grainsize, i))

xs = sorted(xs, key=lambda x: (x[0] + x[1], x[kw == "storlek"]), reverse=True)

print(xs[0][2])