# Abandoned Animal
# https://open.kattis.com/problems/abandonedanimal
# TAGS: array, logic, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/abandonedanimal.md
"""
N = int(input())

K = int(input())

stores = [set() for _ in range(N)]
for _ in range(K):
    i, s = input().split()
    stores[int(i)].add(s)

M = int(input())

items = []
for _ in range(M):
    items.append(input())

def greedy(storelist, itemlist):
    S_MAX = len(storelist)
    I_MAX = len(itemlist)
    i_s, i_i = 0, 0
    res = []
    while i_s < S_MAX and i_i < I_MAX:
        while i_i < I_MAX:
            if itemlist[i_i] in storelist[i_s]:
                res.append(i_s)
                i_i += 1
            else:
                i_s += 1
                break
    return res

# Step 1 - try the greedy approach
forward = greedy(stores, items)
if len(forward) != M:
    print("impossible")
else:
    # Step 2 - try the backward/time reversed greedy approach
    backward = greedy(stores[::-1], items[::-1])
    # Step 3 - check the equality as described in notes
    # Update - see Implementation comment:
    # need to remember that the indices in backward are "N-1-i" w.r.t to forward stores list
    if all(f == N - b - 1 for f, b in zip(forward, backward[::-1])):
        print("unique")
    else:
        print("ambiguous")
