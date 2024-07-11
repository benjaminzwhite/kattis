# Terrace Hill
# https://open.kattis.com/problems/terracehill
# TAGS: array, stack
# CP4: 0, Not In List Yet
# NOTES:
"""
It's a variant of the "largest rectangle in skyline" type exercises

Commented code below in notes is a dict based implementation to "see" the logic better
(this implementation is not AC, the dictionary step causes TLE, it's just for explanation)

Here, you store indices "before curr i,x" and then update those that are "visible": in other
words, those that have prev_x >= curr_x, each time you encounter a new x
(i.e. higher peaks to the left, that aren't blocked by intermediate peaks)

Note that, if you study this, it's just mimicking stack popping behavior so you can simplify:
iterate through xs, and look behind through the stack until you match the height of current x
---

# TLE dict-based approach 
res = 0
d = {}

for i, (l, r) in enumerate(zip(xs, xs[1:])):
    if l >= r:
        d[l] = i
    else:
        d = {k:v for k,v in d.items() if k >= r}
        if r in d:
            res += i - d[r]
        d[r] = i

print(res)

"""
n = int(input())
xs = list(map(int, input().split()))

res = 0
stk = []
for i, x in enumerate(xs):
    while stk and stk[-1][1] < x:
        stk.pop()
    if stk and stk[-1][1] == x:
        res += i - (stk[-1][0] + 1)
        stk.pop() # Note that this gracefully handles the below logic of ALWAYS appending the current (i,x) -> by popping if stk[-1][1] == x, you replace the "old previously seen x_old value at small index i_old" with (i_new,x_new) on the stack
    stk.append((i, x))

print(res)