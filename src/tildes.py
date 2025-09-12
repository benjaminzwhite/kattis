# Tildes
# https://open.kattis.com/problems/tildes
# TAGS: union find, interpreter, improve
# CP4: 2.4b, Union-Find
# NOTES:
"""
TODO: IMPROVE: note that this is an early implementation of union find (in Python, after reading Halim book).

I implemented based on 1-for-1 adapting the walkthrough of the C++ code in the book; I left comments etc.

Note that it doesn't implement the "path compression" trick to speed up queries, so it runs quite slow
(2+ seconds on Kattis, some other Python solutions are 0.5 seconds).
"""
class UnionFind():

    def __init__(self, N):
        # initially N disjoint sets, each set represented by its sole member: i itself
        # {0} {1} {2} ... {N-1}
        self.parents = list(range(N))
        
        # rank is used to optimized union_set operation - keeps tree size small
        self.rank = [0 for _ in range(N)]
        
        # helper to record how many elements are currently in each set
        # NOTE: since this is accessed by querying indices according to set_size[find_set(i)]
        # then after performing union operations, the size info for "discarded" sets is not updated and therefore is MEANINGLESS
        # i.e. after several union operations, the sum of set_size[] can be > N, but the sum of the set_sizes[] of the CURRENT REPRESENTATIVES will be N
        self.set_size = [1 for _ in range(N)]

        # helper to record how many sets there are currently: -=1 each time you do union_set
        self.num_sets = N

    def find_set(self, i):
        # TODO: NOTE THIS DOES NOT IMPLEMENT THE PATH COMPRESSION TECHNIQUE TO SPEED UP SUBSEQUENT QUERIES SEE p130
        # what set does i belong to? (Where the set it belongs to is labelled according to its representative)
        if self.parents[i] == i:
            return i
        else:
            return self.find_set(self.parents[i])

    def is_same_set(self, i, j):
        # i and j are in same set if they both have the same representative element
        return self.find_set(i) == self.find_set(j)

    def num_disjoint_sets(self):
        # helper - tracks how many disjoint sets we have currently
        return self.num_sets

    def size_of_single_set(self, i):
        # what is the size of the entire set that contains the element i
        # NOTE!! the UP TO DATE size information in the set_size[] list is ONLY STORED AT THE INDEX OF THE SET REPRESENTATIVE
        # IF YOU JUST LOOKUP set_size[i] YOU WILL GET OUT OF DATE INFORMATION
        # You need to look up the set i's representative, using find_set(i), then look up that elements' set_size
        return self.set_size[self.find_set(i)]

    def union_set(self, i, j):
        # the main work of union find data structure
        # obviously if i,j already in same set, dont need to union their sets
        if self.is_same_set(i, j):
            return
        else:
            # find the representative of i and j respectively
            r_i = self.find_set(i)
            r_j = self.find_set(j)
            # rank trick/optimization for keeping tree height small:
            # want to merge the set with the smaller rank into the one with the larger rank
            # WLOG use "r_j" as the label for set with LARGER rank
            if self.rank[r_i] > self.rank[r_j]: # TODO: can add tiebreak == and then decide to tiebreak on LABEL BEING BIGGER ALSO so that e.g. always use bigger label of (i,j) when the 2 have same rank?? just for consistency
                r_i, r_j = r_j, r_i
            # now place the set labelled by r_i UNDER THE SET labelled by r_j
            # r_j always (see above swap() step) is the set with larger rank
            self.parents[r_i] = r_j
            # keep the rank information updated for the speedup
            if self.rank[r_i] == self.rank[r_j]:
                self.rank[r_j] += 1 # e.g imagine (1)<---2 and (3)<---4 became   2--->(1)<---3<---4 note on RHS how you have +=1 height in the new tree from 4 to 1
            # combine the set sizes at r_j
            # NOTE!!! see above, do not update at r_i SO SET_SIZES MUST BE ACCESSED VIA find_set TO GET UP TO DATE INFO
            self.set_size[r_j] += self.set_size[r_i]
            self.num_sets -= 1 # each union_set operation reduces number of sets by 1

# --- Exercise starts here ---
n, q = map(int, input().split())

uf = UnionFind(n + 1) # CARE! 1-based indexing

for _ in range(q):
    op, *vals = input().split()
    if op == 't':
        a, b = map(int, vals)
        uf.union_set(a, b)
    else:
        a = int(vals[0])
        print(uf.size_of_single_set(a))