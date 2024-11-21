# A1 Paper
# https://open.kattis.com/problems/a1paper
# TAGS: logic, nice, improve
# CP4: 3.3c, Ternary Search & Others
# NOTES:
"""
TODO: IMPROVE: I wonder if there is analytical solution.

Nice reasoning exercise. Basically the idea is (to avoid tricky counting of fractional parts of areas and their boundaries):

-> at each step/paper size, we must increase the total tape used BY AT LEAST THE LENGTH OF THE CURRENT MAX SIZE (e.g. A2, then A3,...)
-> now, if we have more available papers than needed to tile this current location, we are done - no need to increase tape any more since already included above
-> HOWEVER, if we have to use smaller papers, we will then increase the result BY THEIR length also so we continue

Note the edge cases that are illuminating:

e.g. A2 + 1000's of A3s -> add A2 len, then A3 len and we are done
e.g. 0 A2, 0 A3 but 1000's of A4's -> need 8* A4's; think about how the above algorithm reflects the additon of tape length at each step OK
"""
n = int(input())

papers = map(int, input().split())

qty = 2 # start at A2; need 2 A2's to perfect match and get A1
curr_l, curr_w = pow(2, -3/4), pow(2, -5/4)
res = 0
ok = False

for avail in papers:
    # assume perfect solve here:
    # we would need to increase tape by: current length * number of shared lenghts (this is 1/2 of the current qty needed to form a perfect solve)
    res += curr_l * (qty // 2)
    # check if it was a perfect solve:
    if avail >= qty:
        ok = True
        break
    # if not we continue
    leftover = qty - avail
    qty = 2 * leftover
    curr_l, curr_w = curr_w, curr_l
    curr_w /= 2

if ok:
    print(res)
else:
    print("impossible")