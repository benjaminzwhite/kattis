# Zagrade
# https://open.kattis.com/problems/zagrade
# TAGS: stack, mathematics, combinatorics
# CP4: 3.2f, Iterative (Combination)
# NOTES:
"""
WA on first submit - you need to take set() of res, since it doesn't want duplicates O_o

Also DO NOT INCLUDE THE INPUT string i.e. with 0 of the brackets removed - hence only do combinations(...,r) with r > 0 i.e. r=1,2,..num of bracket pairs.

Basically just brute force - get the ( bracket ) pairings via a stack approach to get a dict, d, of open:close indices
then take all r=1,2,... combinations of those opening brackets, remove them (and their corresponding closing brackets)
from the string then join the leftover string.

Implementation note:

"avoids" contains all the KEYS from combination AND THEIR CORRESPONDING values d[k] for c in c, the 2 | <-- union of the 2 sets
"""
from itertools import combinations

s = input()
stk = []
d = {}

for i, c in enumerate(s):
    if c == '(':
        stk.append(i)
    elif c == ')':
        k = stk.pop()
        d[k] = i

res = []
for r in range(1, len(d) + 1):
    for c in combinations(d, r):
        avoids = {*c} | {d[k] for k in c}
        curr = ''.join(s[i] for i in range(len(s)) if i not in avoids)
        res.append(curr)

res = sorted(set(res))

for expression in res:
    print(expression)