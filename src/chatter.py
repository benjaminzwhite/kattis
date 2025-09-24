# Chatter
# https://open.kattis.com/problems/chatter
# TAGS: union find, improve
# CP4: 2.4b, Union-Find
# NOTES:
"""
Implementation note: this UnionFind class is based on the C++ version in Halim CP4 book.

However, here I modified it to include another step when doing the update_set: I actually set the "merged set size" to 0.

self.set_size[r_i] = 0 # here r_j will be the one that is "increased", while r_i is the "old set" (see code for this to make sense)

I added it myself as a way to track the actual set sizes.
-> Added it because this exercise asks you to print the specific set sizes for all the sets
-> This means that `self.set_size` now contains the actual set sizes, labeled by their representative
i.e. sum(self.set_size) is == N at all times.

TODO: IMPROVE: I didn't write many tests to make sure that this logic works for edge cases etc. but I get AC on this exercise in any case.

---

Exercise has weird string formatting + sorting requirements for final answer O_o

CARE! Also, reading comprehension: you DO NOT use the seed value r as first x value, you have to do f(r) to get first ever x
"""
class UnionFind():

    def __init__(self, N):
        self.parents = list(range(N))
        self.rank = [0 for _ in range(N)]
        self.set_size = [1 for _ in range(N)]
        self.num_sets = N

    def find_set(self, i):
        if self.parents[i] == i:
            return i
        else:
            return self.find_set(self.parents[i])

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
            # UPDATE TO MY UNIONFIND IMPLEMENTATION:
            self.set_size[r_i] = 0 # TBC CHECK THIS WORKS: I added it myself as a way to track the actual set sizes
            # ------
            self.num_sets -= 1

# --- Exercise starts here ---
import sys
from collections import Counter

for l in sys.stdin:
    n, r, a, b, c = map(int, l.split())

    f = lambda r_: (r_ * a + b) % c

    uf = UnionFind(n)

    for _ in range(n):
        while True:
            r = f(r) # CARE! reading comprehension, need to do f(r) first
            x = r % n
            r = f(r)
            y = r % n
            if x != y:
                break
        uf.union_set(x, y)

    cnt = Counter(x for x in uf.set_size if x > 0) # SEE UPDATE/NOTES about how my UnionFind class now tracks uf.set_size values correctly.

    # REST OF SOLUTION IS JUST FORMATTING FROM NOW ON zzzzzz
    tmp = sorted(cnt.items(), key=lambda t: -t[0])

    res = [uf.num_disjoint_sets()]

    for size, freq in tmp:
        if freq > 1:
            res.append(f"{size}x{freq}")
        else:
            res.append(size)

    print(*res)