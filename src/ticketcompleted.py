# Ticket Completed?
# https://open.kattis.com/problems/ticketcompleted
# TAGS: union find, mathematics, combinatorics
# CP4: 0, Not In List Yet
# NOTES:
"""
Solve with Union-Find. The probability part is: "how many ways to select 2 from each UnionFind-final set"

e.g if after UF you have 3 sets of sizes 4,5 and 8 respectively then number of valid ticket pairs is sum of:

comb(4,2) + comb(5,2) + comb(8,2)

and "ALL possible tickets" is: comb(N,2) where N is initial number of nodes (here N=4+5+8)
and the probability is just dividing numerator by denominator.

NOTES: I needed to use my own implementation of UF.set_size which ACTUALLY TOGGLES set sizes to 0 once they
are MERGED WITH ANOTHER so that, at all times, we have sum(set_sizes) == N
[Halim CP4 book code doesn't seem to implement this]
"""
class UnionFind():

    def __init__(self, N):
        self.parents = list(range(N))
        self.rank = [0 for _ in range(N)]
        self.set_size = [1 for _ in range(N)]
        self.num_sets = N

    # find_set WITHOUT PATH COMPRESSION
    def find_set_no_path_compression(self, i):
        if self.parents[i] == i:
            return i
        else:
            return self.find_set_no_path_compression(self.parents[i])

    # based on the code of CP4 Halim book, after studying the path compression speedup:
    # https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
    def find_set(self, i):
        parent_i = i
        children = []
        while parent_i != self.parents[parent_i]:
            children.append(parent_i)
            parent_i = self.parents[parent_i]
        # this is the path compression bit, speeds up future queries
        for c in children:
            self.parents[c] = parent_i
        return parent_i

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def num_disjoint_sets(self):
        return self.num_sets

    def size_of_single_set(self, i):
        return self.set_size[self.find_set(i)]

    def union_set(self, i, j):
        if self.is_same_set(i, j):
            return
        else:
            r_i = self.find_set(i)
            r_j = self.find_set(j)
            if self.rank[r_i] > self.rank[r_j]:
                r_i, r_j = r_j, r_i
            self.parents[r_i] = r_j
            if self.rank[r_i] == self.rank[r_j]:
                self.rank[r_j] += 1
            self.set_size[r_j] += self.set_size[r_i]
            # ------
            # Update to UnionFind implementation for this exercise:
            self.set_size[r_i] = 0 # now we track the actual set sizes
            # ------
            self.num_sets -= 1


N, M = map(int, input().split())

UF = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    UF.union_set(a, b)

res = 0

for x in UF.set_size:
    res += x * (x - 1) // 2

print(res / (N * (N - 1) / 2))