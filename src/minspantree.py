# Minimum Spanning Tree
# https://open.kattis.com/problems/minspantree
# TAGS: graph, tree, MST
# CP4: 4.3a, MST, Standard
# NOTES:
"""
CARE! You need to check that there is indeed == 1 connected component for it to be a spanning tree.
I was getting WA until doing this so it seems that you can end up with some testcases
generating 2,3.. disconnected trees with V-1 edges in total which are NOT MSTs.
"""
class UnionFind():

    def __init__(self, N):
        self.parents = list(range(N))
        self.rank = [0 for _ in range(N)]
        self.set_size = [1 for _ in range(N)]
        self.num_sets = N

    # based on the code of CP4 Halim book, after studying why the path compression leads to speedup:
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
        if self.is_same_set(i,j):
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
            self.set_size[r_i] = 0
            # ------
            self.num_sets -= 1


while True:
    V, E = map(int, input().split())
    if V == E == 0:
        break
    edges = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges = sorted(edges, key = lambda x: x[0])

    uf = UnionFind(V)
    vertices = []
    res = 0

    for w, u, v in edges:
        if not uf.is_same_set(u, v):
            res += w
            vertices.append(tuple(sorted([u, v])))
            uf.union_set(u, v)
        if len(vertices) == V - 1:
            break

    if vertices and uf.num_disjoint_sets() == 1: # CARE! Need to ALSO CHECK THAT RESULTING "Tree" IS INDEED A TREE i.e has only 1 connected component
        print(res)
        for u, v in sorted(vertices, key = lambda x: (x[0], x[1])):
            print(u, v)
    else:
        print("Impossible")
