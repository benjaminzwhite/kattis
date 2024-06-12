# Safe Passage
# https://open.kattis.com/problems/safepassage
# TAGS: logic
# CP4: 4.6a, S/Longest Paths on DAG
# NOTES:
"""
It's the classic interview "bridge crossing with torch problem".
See #7 in Anany Levitin - Algorithmic Puzzles book also or wiki:
https://en.wikipedia.org/wiki/Bridge_and_torch_problem

---

Implementing the theorem and case studies from:

http://page.mi.fu-berlin.de/rote/Papers/pdf/Crossing+the+bridge+at+night.pdf

Crossing the Bridge at Night - Gunter Rote
"""
def f(xs):
    n = len(xs)
    
    if n == 1: # not needed in our case since n>=2 always
        return xs[0]
    elif n == 2:
        return xs[1]
    elif n == 3:
        return sum(xs)
    else:
        return f(xs[:-2]) + xs[0] + xs[-1] + min(2 * xs[1], xs[0] + xs[-2])

_, *xs = map(int, input().split())

# sort first - should put this in the function logic really
xs = sorted(xs)

print(f(xs))