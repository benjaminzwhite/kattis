# Zigzag (note this is Zigzag 2 there must be another one on Kattis called zigzag O_o)
# https://open.kattis.com/problems/zigzag2
# TAGS: greedy, proof
# CP4: 0, Not In List Yet
# NOTES:
"""
Saw difficulty was 5+ so I spent a while thinking about a sophisticated solution but "greedy" solution is always optimal.

On paper I drew something like this:

   _ _ _ _ X1 _ _ X2 _ _ _ X3 _
             inc    dec

Where X_i represents that the values that are in a/the max length solution and inc dec refers to whether that interval from X1->X2 is with X1<X2 or >

-> if this is optimal then there can't be e.g. a X99 such that X1 > X99 < X2 (draw on paper an arrow going "down" to X99 and then "up" to X2)
   because otherwise you could += the length of the solution contradicting its optimality
   --> so X1->X2 is made up only of elements that are non-decreasing
 -> same for all the intervals in the final optimal length solution, so basically you just count nondecreasing/nonincreasing subsequences from left to right, 
    and toggle inc/dec when you reach the rightmost (largest or smallest) since it is never wrong to use the highest high or lowest low for the optimal subsequence

    e.g in 2 4 9 30 55 1: you can have length 3 with 2 4 1 or 2 55 1, never wrong to use the largest in the given nondecreasing subsequence under consideration

---

Implementation notes:

Make sure you handle "1 1 1 1 1" example correctly, below I check that at least one pair l,r is != so this sets flg to 1

Can improve by just processing pairwise "previous, current" element instead of taking into xs list (not needed to store)
(May need to do this if timelimit changes/input speed changes O_o)
"""
n = int(input())

xs = []
for _ in range(n):
	xs.append(int(input()))

res = 1
flg = 0
climbing = -1
for l, r in zip(xs, xs[1:]):
    if l != r:
        flg = 1
    if r < l:
        res += (climbing == 1)
        climbing = 0
    elif r > l:
        res += (climbing == 0)
        climbing = 1

print(res + flg)