# Arctic Network
# https://open.kattis.com/problems/arcticnetwork
# TAGS: graph, tree, MST
# CP4: 4.3b, MST, Variants
# NOTES:
"""
The description is a bit confusing, but basically the idea is:

You are finding "MST" but instead of stopping when there is EXACTLY 1 connected component, you can
stop when there are num_channels connected components (these can then talk to eachother by satellite or w/e the description is)

So do Kruskal's, until unionFind has num_channels disjoint sets:

- at each step when you add edge with curr weight = w,
then that is the HIGHEST DISTANCE WITHIN ANY OF THE CONNECTED COMPONENTS (which need to be connected by cables, not satellite)
so that is your answer.

It's the largest "physical" distance that must be built, everything larger can be covered by the num_channels satellites coverage etc
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
            self.set_size[r_i] = 0
            # ------
            self.num_sets -= 1

# --- Queries ---
T = int(input())
for _ in range(T):
    num_channels, V = map(int, input().split())
    xs = []
    for _ in range(V):
        x, y = map(float, input().split())
        xs.append((x, y))

    edges = []
    for i in range(V):
        for j in range(i + 1, V):
            x1, y1 = xs[i]
            x2, y2 = xs[j]

            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            edges.append((d, i, j))

    uf = UnionFind(V)
    res = 0
    edges = sorted(edges, key = lambda x: x[0])
    for w, u, v in edges:
        if not uf.is_same_set(u, v):
            res = w
            uf.union_set(u, v)
            if uf.num_disjoint_sets() == num_channels:
                break

    print(f"{res:.2f}") # formatting requirements
    