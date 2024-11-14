# Paintings
# https://open.kattis.com/problems/paintings
# TAGS: DFS
# CP4: 3.2k, Backtracking (Easier)
# NOTES:
"""
Since you do DFS by trying to add the "favorite" colors first in descending order of preference, the first time you reach
a painting with N colors you have obtained the Favourite Painting (hard to read description but this is what it means)
i.e. first length N painting found by DFS (by adding colors from preference list Left to Right) is the result the exercise wants

I used flag boolean to save this state/result first time you encounter it
"""
from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    preferences = input().split()

    M = int(input())
    BADS = defaultdict(set)
    for _ in range(M):
        l, r = input().split()
        BADS[l].add(r)
        BADS[r].add(l)

    def dfssolve(curr, avail_indices):
        best = []
        cnt = 0
        found_fav = False

        def dfs(curr, avail_indices):
            nonlocal best, cnt, found_fav
            if len(curr) == N:
                if not found_fav:
                    best = curr
                    found_fav = True
                cnt += 1

            for i, b in enumerate(avail_indices):
                if b:
                    next_color = preferences[i]
                    if not curr or (next_color not in BADS[curr[-1]] and curr[-1] not in BADS[next_color]):
                        new_list = curr + [next_color]
                        avail_indices[i] = False
                        dfs(new_list, avail_indices)
                        avail_indices[i] = True

        dfs(curr, avail_indices)
        
        print(cnt)
        print(' '.join(best))

    initial_indices = [True] * N
    dfssolve([], initial_indices)