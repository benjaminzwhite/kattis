# GCDs
# https://open.kattis.com/problems/gcds
# TAGS: mathematics, number theory, array
# CP4: 8.7c, Fast DS+Other, Easier
# NOTES:
"""
I found it quite hard to understand the statement/reading comprehension.

I don't know why he is talking about indices, values etc.

Here's how I would reformulate question: 

"Given xs e.g. [3,5,61,13,22] if you compute the GCD of all possible contiguous subsequences, how many distinct values of the GCD will you find?"

Important: he also includes "size 1" subsequences! (needed to reverse engineer test-case to understand this)

So for ex: res for [3,7,11] is **4** because gcd(3,7) = 1 gcd(7,11) = 1, gcd(3,7,11) = 1, but gcd(3,3) = 3, gcd(7,7) = 7 and gcd(11,11) = 11 
so res set is {1,3,7,11} -> 4 distinct values O_o

---

So basically I do a DIY reduce:

Take GCD of pairwise elements and use that reduction as the "new xs" on the next iteration:

-> the insight is that you can significantly shorten the size of "new xs" if you only append a
   single "representative" whenever you encounter a stretch with the same GCD

e.g. suppose xs = [...15,60,55,1000...]  then the gcd 15,60 gives 5; gcd 60,55 gives 5, gcd 55,1000 gives 5 etc

So instead of creating xs' with the corresponding block = [ ...5,5,5...] you can just append 5 ONCE since in any
case that contiguous block will only contribute the value '5' to any GCD involving it as a subsequence
(basically "groupby" each xs' after each pass)
"""
from math import gcd

n = int(input())
xs = []
for _ in range(n):
	xs.append(int(input()))

res = set()
while len(xs) > 1:
    # basically just take the 1st, 2nd, 3rd, ... "differences" i.e. the pairwise GCDS:
    # -> can discard at each step contiguous blocks of the same elements (since e.g. ....17,17,17,17,17... will just be reduced <--X--> times always producing 17 as GCD until reach a non-17 value on left or right)
    # -> groupby the xss temp list and update xs to be the groupby keys (see above, this turns 17,17,17,17 to 17 etc)
    # UPDATE: actually, just check last element of xss and compare to curr element != or == ? only append if != [this avoids another pass through xss with groupby, does it on the fly]
    res.update({xs[0]}) # CARE!: below we add the r value in l,r zip, so initial l i.e. xs[0] doesn't get added to res set -> need to do it manually
    xss = []
    for l, r in zip(xs, xs[1:]):
        curr = gcd(l, r)
        res.update({r})
        if not xss or xss[-1] != curr:
            xss.append(gcd(l, r))
    xs = xss

# CARE!: extra case/condition
# need to also consider that the final GCD value in xs when len(xs)==1 has NOT BEEN SEEN BEFORE
print(len(res.union(xs)))