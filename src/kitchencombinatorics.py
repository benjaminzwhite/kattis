# Kitchen Combinatorics
# https://open.kattis.com/problems/kitchencombinatorics
# TAGS: mathematics, combinatorics, brute force
# CP4: 5.4e, Others, Harder
# NOTES:
"""
Just combinatorics, main difficulty is reading comprehension and also dealing with indexing/where the data is.

Basically you have 3 types of courses s/m/d:

- try all products involving 1 of each type i.e. 1 starter 1 main 1 dessert
- except: remove the products which involve one or more incompatible pairings; these are given in input() but it's hard to parse/access

I basically access the incompatible pairs by adjusting their index in the A[] list below:

- the first s items are the starters
- then to get the mains, since there are s starters, mains START at index s + 0
- then for deserts they start at s + m + 0 etc.
"""
from itertools import product

r, s, m, d, n = map(int, input().split())

brands = [0] +  list(map(int, input().split())) # 1 based indexing

A = [[-1]] # 1 based indexing

for _ in range(s):
    _, *i = map(int, input().split())
    A.append(i)
for _ in range(m):
    _, *i = map(int, input().split())
    A.append(i)
for _ in range(d):
    _, *i = map(int, input().split())
    A.append(i)

incompatibles = {}
for _ in range(n):
    fst, snd = map(int, input().split())
    incompatibles[(fst, snd)] = True
    incompatibles[(snd, fst)] = True

res = 0
for s_, m_, d_ in product(range(1, s + 1), range(1, m + 1), range(1, d + 1)):
    if (s_, m_ + s) in incompatibles or (s_, d_ + s + m) in incompatibles or (m_ + s, d_ + s + m) in incompatibles:
        continue

    all_ings = set(A[s_] + A[m_ + s] + A[d_ + s + m])
    tmp = 1
    for i in all_ings:
        tmp *= brands[i]
    res += tmp

if res > 10**18:
    print("too many")
else:
    print(res)