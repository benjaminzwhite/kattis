# Pawn Shop
# https://open.kattis.com/problems/pawnshop
# TAGS: array, greedy
# CP4: 0, Not In List Yet
# NOTES:
"""
Basically greedy works; as soon as you have a sublist of any len such that A[i:j] contains all the same elements as B[i:j] then
you should delimit that B[i:j] and reset to 0 the count and continue through the zip.

Implementation notes:

I'm doing a kind of two-sum approach where I track the needed values (in A) as +1 and assign -1 to the actual seen values (in B)
-> As I iterate through, the condition that we have an equal number of e.g. x=173 in A and in B will occur when d[173] is set to 0 in the dict
-> when d[k] = 0 for any key, delete it from dict; when ALL KEYS HAVE BEEN DELETED FROM DICT, then we know currently processing sublist has been 
   entirely paired off: so now append divisor '#' to res, and continue with empty d={} for next sublist
"""
from collections import defaultdict

N = int(input())
A = map(int, input().split())
B = map(int, input().split())

res = []
d = defaultdict(int)

for a, b in zip(A, B):
    d[a] += 1
    d[b] -= 1
    res.append(b)
    if d[a] == 0:
        del d[a]
    if d[b] == 0:
        del d[b]
    if len(d) == 0:
        res.append('#')

print(*res[:-1])