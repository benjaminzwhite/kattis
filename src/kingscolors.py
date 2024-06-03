# King's Colors
# https://open.kattis.com/problems/kingscolors
# TAGS: mathematics, combinatorics, improve
# CP4: 0, Not In List Yet
# NOTES:
"""
TODO: IMPROVE: see if you can simplify the combinatorial identity O_o

---

Just PIE on the chromatic polynomial of a tree:

- chromatic polynomial; suppose you have k available colors. Color the root in k ways, then for all (n-1) other child nodes you
  can color them freely in (k-1) ways (since can use any except the color of the parent, and don't have to worry
  about cycles/adjacent nodes since it's a tree).

So for PIE, the above chromatic polynomial is the number_of_ways_using_upto_c_colors
-> UPTO(k,n) = k * (k-1) * (k-1) * .... (k-1) = k * (k-1)**(n-1)

We want the result: EXACT(k,n) i.e. those which use exactly k colors across the tree
(since e.g. UPTO(3,4) will include colorings with 2 BUT NOT 3 of the k=3 colors used)

So PIE-remove the bad colorings, where you comb(k, how_many_colors_less_than_k_used):

EXACT(k,n) = comb(k,k) * UPTO(k,n) - comb(k,k-1) * UPTO(k-1,n) + comb(k,k-2) * UPTO(k-2,n) + ....

"""
BIGMOD = 10**9 + 7

from math import comb

def upto(k, n):
    return k * (k - 1)**(n - 1)

n, k = map(int, input().split())

res = sum((-1)**(k - k_) * comb(k, k_) * upto(k_, n) for k_ in range(k, 0, -1))

print(res % BIGMOD)