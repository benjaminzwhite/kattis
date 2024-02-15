# Height Ordering
# https://open.kattis.com/problems/height
# TAGS: array, sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
"""
The solution below is just "actually doing" the steps given.

There is a shorter/more insightful way to get the solution, if you want to code golf it (ask yourself, what
is the number that gets added at each iteration, and what does it correspond to in the original input list?)
"""
P = int(input())
for _ in range(P):
    k, *xs, = map(int, input().split())
    final = [xs[0]]
    steps = 0
    for x in xs[1:]:
        i = next((i for i, y in enumerate(final) if y > x), len(final))
        tmp = len(final) - i
        steps += tmp
        final.insert(i, x)
    print(k, steps)