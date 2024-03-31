# Integer Division
# https://open.kattis.com/problems/integerdivision
# TAGS: array, mathematics, nice
# CP4: 5.4d, Others, Easier
# NOTES:
"""
Nice little exercise:

Look behind for every new x, how many previous x's previously had the same res upon integer divison by d. Increase the acc by this total amount

e.g. for d=4 and xs = 4,5,6,7
x=4 // 4 = 1, and there are 0 prev values that led to 1 so acc += 0, and set counter[1] to 0+1 = 1
x=5 // 4 = 1, there are counter[1]=1 prev values that lead to 1 so acc +=1 and set counter[1] to 1+1=2 now
x=6 // 4 = 1, there are counter[1]=2 prev values that lead to 1 so acc +=2 and set counter[1] to 2+1=3 now
x=7 // 4 = 1, there are counter[1]=3prev values that lead to 1 so acc +=3 and set counter[1] to 3+1=4 now

- Note that this works because it models the fact that for the current x we increment by e.g. counter[1]
(since that is how many previous elements can be "paired with" x)

- Note that this also avoids double counting:
we are always at "index j" with current x, and the counter[1] = 3 means that there are 3 "index i's to the left of j"
so that gets us all pairs with i<j and j as the current element
"""
from collections import defaultdict

n, d = map(int, input().split())
xs = map(int, input().split())

c = defaultdict(int)
acc = 0
for x in xs:
    res = x // d
    acc += c.get(res, 0)
    c[res] += 1

print(acc)