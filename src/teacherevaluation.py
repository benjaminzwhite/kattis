# Teacher Evaluation
# https://open.kattis.com/problems/teacherevaluation
# TAGS: greedy
# CP4: 3.4e, Non Classical, Easier
# NOTES:
from math import ceil

N, P = map(int, input().split())

xs = map(int, input().split())

S = sum(xs)

# If wanted average P is == 100 and all the current students do not have exactly 100 score, then impossible to reach 100 average
if P == 100:
    if S != (N * 100): # UPDATE: rereading exercise it says specifically that this case never occurs i.e never have all scores == 100, so just print IMPOSSIBLE if P==100 in all cases
        print("impossible")
    else:
        print(0) # average is already 100 so need to add 0 tests
else:
    # Greedily add k 100 values until average is >= P; can adjust down to any integer value from there
    # (S + k * 100) / (N + k) >= P
    # rearranging:
    # k >= (P * N - S) / (100 - P)
    k = (P * N - S) / (100 - P)
    print(ceil(k))