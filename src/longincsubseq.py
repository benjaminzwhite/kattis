# Longest Increasing Subsequence
# https://open.kattis.com/problems/longincsubseq
# TAGS: longest increasing subsequence
# CP4: 3.5c, LIS
# NOTES:
"""
You need the O(n log k) solution for this exercise, see p208 Halim CP4.

I looked up their implementation of the P[] list which allows you to 
reconstruct the indices of the values that acually appear in the optimal result

https://github.com/stevenhalim/cpbook-code/blob/master/ch3/dp/LIS.py
"""
from bisect import bisect_left

while True:
    try:
        N = int(input())
        xs = list(map(int, input().split()))

        #N = len(xs)
        last_val_of_LIS_of_len = [float('inf')] * N
        idx_of_last_val_of_LIS_of_len = [-1] * N
        P = [None] * N

        last_idx_for_reconstruct_path = 0
        max_LIS_len = 1
        for i, x in enumerate(xs):
            insert_pos = bisect_left(last_val_of_LIS_of_len, x)
            #print(insert_pos)
            last_val_of_LIS_of_len[insert_pos] = x
            idx_of_last_val_of_LIS_of_len[insert_pos] = i
            if insert_pos + 1 > max_LIS_len:
                max_LIS_len = insert_pos + 1
                last_idx_for_reconstruct_path = i
            P[i] = idx_of_last_val_of_LIS_of_len[insert_pos - 1] if insert_pos > 0 else -1

        res_indices = []
        while P[last_idx_for_reconstruct_path] >= 0:
            res_indices.append(last_idx_for_reconstruct_path)
            last_idx_for_reconstruct_path = P[last_idx_for_reconstruct_path]
        res_indices.append(last_idx_for_reconstruct_path)

        print(len(res_indices))
        print(*res_indices[::-1])
    except:
        break