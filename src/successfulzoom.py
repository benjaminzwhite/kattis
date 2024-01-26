# Successful Zoom
# https://open.kattis.com/problems/successfulzoom
# TAGS: array
# CP4: 3.2g, Try All Answers
# NOTES:
"""
- Below approach is unoptimized but logic is clear; you can avoid sorting/more concise if you want to code golf also
"""
n = int(input()) # n = len(xs)

xs = list(map(int, input().split()))

flg = True
for d in range(1, n // 2 + 1):
    if (X := xs[d-1::d]) == sorted(X) and (len(set(X)) == len(X)):
        print(d)
        flg = False
        break

if flg:
    print("ABORT!")