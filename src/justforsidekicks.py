# Just for Sidekicks
# https://open.kattis.com/problems/justforsidekicks
# TAGS: Fenwick tree
# CP4: 2.4c, Tree-related DS
# NOTES:
"""
The basic idea is simple: use a Fenwick tree for each of the 6 classes.

However there's  0/1-based indexing stuff that's mixed up, so the implementation
is a bit confusing.

The Fenwick tree code here is based on the Halim CP4 book C++ implementation.
"""
def LSOne(n):
    """
    returns value of least significant set bit of n 

    example: LSOne(90) = LSOne(10110|1|0) = 2**1 = 2
    """
    return n & (-n)


class FenwickTree():

    def __init__(self, m):
        # m keys
        self.ft = [0] * (m + 1) # creates the empty Fenwick array

    def rsq_to_right(self, j):
        res = 0
        while j > 0:
            res += self.ft[j]
            j -= LSOne(j)
        return res

    def rsq(self, i, j):
        return self.rsq_to_right(j) - self.rsq_to_right(i - 1)

    def update(self, i, val):
        # updates value of the i'th element of the fenwick array ft[] by val
        # NOTE: val can be positive or negative
        M = len(self.ft)
        while i < M:
            self.ft[i] += val
            i += LSOne(i)

# --- Exercise starts here ---
N, Q  = map(int, input().split())

# create 6 Fenwick trees
# NOTE: in my implementation the "first" Fenwick tree is at FTS[0]
# so this needs some "i-1" type indexing modifications in the
# main queries processing part below
FTS = [FenwickTree(N) for _ in range(6)]

values = list(map(int, input().split()))

gem_types = list(map(int, list(input())))

# care 0/1-based indexing here -.-
for i, gtype in enumerate(gem_types, 1):
    FTS[gtype - 1].update(i, 1)

for _ in range(Q):
    query_type, fst, snd = map(int, input().split())
    if query_type == 2:
        values[fst - 1] = snd
    elif query_type == 1:
        old_gem = gem_types[fst - 1]
        FTS[old_gem - 1].update(fst, -1)
        FTS[snd - 1].update(fst, 1)
        gem_types[fst - 1] = snd
    else:
        res = 0
        for ft in range(6):
            tmp = FTS[ft].rsq(fst, snd)
            res += tmp * values[ft]
        print(res)