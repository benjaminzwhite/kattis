# Dirty Driving
# https://open.kattis.com/problems/dirtydriving
# TAGS: array, sorting
# CP4: 2.2f, Sorting, Harder
# NOTES:
"""
Reading comprehension:

A bit of a confusing exercise since, as far as I can understand, the n in description IS NOT THE SAME n AS IN THE INPUTS SECTION !?!?
"""
_, p = map(int, input().split())
xs = sorted(map(int, input().split()))

max_dist = 0

for i, x in enumerate(xs):
    max_dist = max(max_dist, p * (i + 1) - x)

res = max_dist + xs[0] # CARE! need to add distance to the car "IMMEDIATELY IN FRONT OF YOU" which is therefore xs[0] since xs is sorted

print(res)