# Pianino
# https://open.kattis.com/problems/pianino
# TAGS: array, nice
# CP4: 0, Not In List Yet
# NOTES:
"""
I wrote a detailed solution:

https://github.com/benjaminzwhite/kattis/blob/main/detailed_solutions/pianino.md
"""
N = int(input())

xs = list(map(int, input().split()))

d = {}
fst = xs[0]
acc_up_down = 0
ALL_KS_DUE_TO_acc_up_down_hit_zero = 0 # variable named to match the variable described in notes above O_o

for l, r in zip(xs, xs[1:]):
    if r < l:
        acc_up_down -= 1
    if r > l:
        acc_up_down += 1

    # which value of K, if any, would score here?
    if acc_up_down == 0:
        if r == fst:
            ALL_KS_DUE_TO_acc_up_down_hit_zero += 1
            #d[0] = 1 + d.get(0, 0) SEE UPDATES: this leads to weird max_v calculations/subtle error
    else:
        # if the AMOUNT difference between curr r and fst value in xs is delta = r - fst, and we are at "+2" up moves relative to start
        # then the only K value that would score here, if any, is delta//2 [and only if this division can be done in integers with no remainder]
        q, rem = divmod(r - fst, acc_up_down)
        if rem == 0:
            d[q] = 1 + d.get(q, 0)

# SEE UPDATE: this is where you have to be careful if you track d[k=0] separately - simpler to just treat 0 as the default k value
# and then, if no other k beats 0, final result will be 1 + 0 + ALL_KS so handled nicely.
max_k, max_v = 0, 0
for k, v in d.items():
    if v > max_v:
        max_k = k
        max_v = v

print(1 + max_v + ALL_KS_DUE_TO_acc_up_down_hit_zero)
print(max_k)