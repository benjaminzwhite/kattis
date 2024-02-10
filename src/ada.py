# The Calculus of Ada
# https://open.kattis.com/problems/ada
# TAGS: mathematics
# CP4: 5.2h, Polynomial
# NOTES:
"""
It is guaranteed that not all xs are same i.e. no inputs of the form 8 8 8 8 8, which would correspond to d=0

---

Implementation note:

You don't need to store in diffs the lists from each step of the while loop, it's just for clarity below
(can just get the last value of xs at each step of the loop directly and incremement total result)
"""
n, *xs, = map(int, input().split())

d = 1
diffs = [xs]
while True:
    xs = [b - a for a, b in zip(xs, xs[1:])]
    diffs.append(xs)
    if len(set(xs)) == 1: # how I implement the end condition i.e. when all terms have same difference
        break
    else:
        d += 1

# --> The next term in the series is the sum of the last element in each of the lists in diffs
# (visualize the cascading diagram of finite differences; all the rightmost terms in the pyramid produce the next term in the sequence)
print(d, sum(a[-1] for a in diffs))