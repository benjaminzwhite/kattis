# Odd Gnome
# https://open.kattis.com/problems/oddgnome
# TAGS: basic, array
# CP4: 1.4i, Control Flow, Level 3
# NOTES:
"""
Note: I got a Run Time Error which I didn't understand, given it is simple exercise, but
then I realized it's because I was using itertools.pairwise, which isn't available
in Python 3.8 used by Kattis.
"""
n = int(input())

for _ in range(n):
    g, *xs = map(int, input().split())
    xs = list(xs)
    for i in range(1, g):
        if xs[i] != xs[i - 1] + 1:
            print(i + 1) # CARE! 1-based indexing
            break