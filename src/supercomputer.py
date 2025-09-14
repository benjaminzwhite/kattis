# Supercomputer
# https://open.kattis.com/problems/supercomputer
# TAGS: Fenwick tree, interpreter, improve
# CP4: 2.4c, Tree-related DS
# NOTES:
"""
This Fenwick tree implementation is based on the C++ version in Halim CP4 book (section 2.4.3), might not be optimal.

TODO: IMPROVE: clear up the +/-1 indexing confusion.

---

CARE! we are not updating the state of the flipped bits 0/1 by accessing the fenwick_tree.ft[] array but:
Instead I store the ACTUAL state of the system in a separate array f[], this says whether current bit i is ON or OFF.
Then the Fenwick Tree is to be updated, depending on the state of f[i].
"""
# helper binary bitwise manipulation function
def LSOne(n):
    """
    returns value of least significant set bit of n 

    example: LSOne(90) = LSOne(10110|1|0) = 2**1 = 2
    """
    return ((n) & -(n))

class FenwickTree():

    def __init__(self, m):
        # m keys
        # CARE! 1-based indexing here ?
        self.ft = [0 for _ in range(m + 1)] # creates the empty Fenwick array

    def rsq_to_right(self, j):
    	# rsq: range sum query
        res = 0
        while j > 0:
            res += self.ft[j]
            j -= LSOne(j)
        return res

    def rsq(self, i, j):
    	# CARE! i-1 for indexing
        return self.rsq_to_right(j) - self.rsq_to_right(i - 1)

    def update(self, i, val):
        # updates value of the i'th element of the fenwick array ft[] by val
        # NOTE: val can be positive or negative
        M = len(self.ft)
        while i < M:
            self.ft[i] += val
            i += LSOne(i)

# --- Exercise starts here ---
N, Q = map(int, input().split())

# CARE! I store the **state of the bits** like this, the Fenwick Tree updates are separate
f = [0] * (N + 1)

# CARE! 1 based indexing [update; FenwickTree class does this already, but to avoid confusion O_o N+1 here]
fenwick_tree = FenwickTree(N + 1)

for _ in range(Q):
    op, *vals = input().split()
    if op == 'F':
        i = int(vals[0])
        if f[i] == 1:
            fenwick_tree.update(i, -1)
            f[i] = 0
        else:
            fenwick_tree.update(i, 1)
            f[i] = 1
    else:
        l, r = map(int, vals)
        print(fenwick_tree.rsq(l, r))