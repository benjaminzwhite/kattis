# Birthday Memorization
# https://open.kattis.com/problems/fodelsedagsmemorisering
# TAGS: dict
# CP4: 2.3h, Balanced BST (map)
# NOTES:
"""
Can shorten the logic using a single or, but left the layout below for clarity.
"""
d = {}
n = int(input())

for _ in range(n):
    name, score, date = input().split()
    score = int(score)
    if date not in d:
        d[date] = (score, name)
    else:
        if d[date][0] < score:
            d[date] = (score, name)

res = sorted(v[1] for k, v in d.items()) # can just use d.values() O_o

print(len(res)) # CARE! it wants you to print the number of names res before the names themselves
for name in res:
    print(name)