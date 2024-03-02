# Red Rover
# https://open.kattis.com/problems/redrover
# TAGS: string, brute force
# CP4: 6.4a, String Matching
# NOTES:
"""
Just try all possible substrings and try replacing each one in the input string with the macro symbol 'M'

CARE! you also need to consider that L might be the min length result - this is the case for s="NSEW" for example.

So initialize best = len(s) (or take min(best, len(s)) at the end of loop).

This way, if the loop produces best > len(s) you cover this case. (Loop produces best = 5 for "NSEW" for example)

---

You can solve this much more intelligently if you want to code golf also.
"""
s = input()

best = len(s)

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        macro = s[i:j]
        t = s.replace(macro, 'M')
        best = min(best, len(macro) + len(t))

print(best)