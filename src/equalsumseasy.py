# Equal Sums (Easy)
# https://open.kattis.com/problems/equalsumseasy
# TAGS: brute force, bitmask
# CP4: 8.6a, NP-hard/C, small, E
# NOTES:
"""
- Use bitmask to iterate over subsets
"""
T = int(input())

for t in range(1, T + 1):
    print(f"Case #{t}:")

    N, *xs, = map(int, input().split())
    res = {}
    flg = True

    for mask in range(1 << N):
        curr_indices = []
        curr_sum = 0
        for i in range(N):
            if mask & (1 << i):
                curr_sum += xs[i]
                curr_indices.append(i)
        if curr_sum in res:
            print(*(xs[i] for i in res[curr_sum]))
            print(*(xs[i] for i in curr_indices))
            flg = False
            break
        else:
            res[curr_sum] = curr_indices

    if flg:
        print("Impossible")