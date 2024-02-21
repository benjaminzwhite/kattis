# Zyxab
# https://open.kattis.com/problems/zyxab
# TAGS: basic
# CP4: 0, Not In List Yet
# NOTES:
"""
CARE! Note that it wants "ASCENDING ORDER" basically the opposite of usual
lexicographic sort order in case of tiebreak on length(x)
"""
n = int(input())

best = None

for _ in range(n):
    s = input()
    if len(s) >= 5 and len(set(s)) == len(s):
        if best is None or len(s) < len(best):
            best = s
        elif len(s) == len(best):
            if s > best:
                best = s

if best is None:
    print("neibb!")
else:
    print(best)