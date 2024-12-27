# Stop Counting!
# https://open.kattis.com/problems/stopcounting
# TAGS: array
# CP4: 3.2i, Math Simulation, Harder
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/stopcounting.md
"""
N = int(input())
xs = list(map(int, input().split()))

best_sum = 0
best_cnt = 0

l_to_r_acc = 0
for curr_cnt, x in enumerate(xs, 1):
    # Implementation note: avoid floats by rewriting:
    # sum(curr_vals) / cnt(curr_vals) >= best_sum / best_cnt
    # as:
    # best_cnt * sum(curr_vals) >= best_sum * cnt(curr_vals)
    l_to_r_acc += x
    if (best_cnt * l_to_r_acc) >= (best_sum * curr_cnt):
        best_sum, best_cnt = l_to_r_acc, curr_cnt

r_to_l_acc = 0
for curr_cnt, x in enumerate(xs[::-1], 1):
    r_to_l_acc += x
    if (best_cnt * r_to_l_acc) >= (best_sum * curr_cnt):
        best_sum, best_cnt = r_to_l_acc, curr_cnt

if best_sum <= 0:
    print(0) # choose no cards option if all options lead to negative average
else:
    print(best_sum / best_cnt)