# Saving the Universe
# https://open.kattis.com/problems/savinguniverse
# TAGS: interpreter
# CP4: 4.6a, S/Longest Paths on DAG
# NOTES:
"""
This seems to be basically the same thing as
https://open.kattis.com/problems/colorland
I already solved

---

Implementation notes:
Basically "search for the search engine which is FURTHEST IN THE FUTURE from now i.e. with highest index"
-> append float('inf') to all engine's dequeues, which represents there NOT BEING ANY MORE OF THAT SEARCH ENGINE IN THE LIST
-> i.e. once the head of the deque is float('inf') you know there are no more appearances of "Google" so can use that for all subsequent queries

---

After solving this way, I realised you can make it much shorter (hint: just track how many engines are currently "seen")
"""
from collections import deque

T = int(input())
for t in range(1, T + 1):
    S = int(input())
    d = {}
    for _ in range(S):
        s = input()
        d[s] = deque([])

    Q = int(input())
    for i in range(Q):
        q = input()
        d[q].append(int(i))

    for k, v in d.items():
        v.append(float("inf"))  # if next index can ever reach float("inf") it means no more appearances of this search engine, so can use it with 0 swaps needed from this point

    swaps = 0
    curr_idx = -1
    curr_engine = None
    while curr_idx < Q:
        for k, v in d.items():
            if v[0] > curr_idx and k != curr_engine:
                curr_engine = k
                curr_idx = v[0]
        if curr_idx == float("inf"):
            break
        else:
            swaps += 1
            for k, v in d.items():
                while v[0] < curr_idx: # CARE! < rather than <= (gets WA otherwise)
                    v.popleft()

    print(f"Case #{t}: {swaps}")