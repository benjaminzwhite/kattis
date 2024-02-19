# Kolone
# https://open.kattis.com/problems/kolone
# TAGS: logic, improve
# CP4: 6.2f, Really Ad Hoc
# NOTES:
"""
TODO: IMPROVE - below is the "implement the algorithm" approach; there must be an analytical
solution but I didn't see it immediately when solving.

---

The logic is that (if you draw a diagram where the Lefts and Rights are initially facing) you originally have 1 index at which to perform a swap
Then, you will perform next swap at idx+1 and idx-1 (SO LONG AS THEY ARE IN THE BOARD)
But also, you will only perform swaps as long as there is a Rightfacing ant in the left range and or a Leftfacing ant in the right range
So I track the leftmost Rightfacing and rightmost Leftfacing ants.

Test cases with M=1 and N=x are hard edge cases, also note that you must:
+= leftmost once you "see it" i.e. once you reach i=its index
-= rightmost once you see (RIGHTMOST - 1) <--- Note the -1 !!! This caused me WA on first submit.
(Why? Because you flip from i to i+1, so look for rightmost-1 rather than rightmost)
"""
M, N = map(int, input().split())
s1 = input()
s2 = input()
T = int(input())

s = list(s1[::-1] + s2)
indices = set({M - 1}) # initially there will be only one swap, it's at the interface between the M rightfacing ants and the N leftfacing ants
leftmost = 0
rightmost = (M + N) - 1

for _ in range(T):
    tmp = set()
    for i in indices:
        if leftmost < i:
            tmp.add(i - 1)
        if leftmost == i:
            leftmost += 1
        if i < rightmost - 1:
            tmp.add(i + 1)
        if rightmost-1 == i:
            rightmost -= 1
        s[i], s[i + 1] = s[i + 1], s[i]
    indices = tmp

print(''.join(s))