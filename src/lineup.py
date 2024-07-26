# Line Them Up
# https://open.kattis.com/problems/lineup
# TAGS: basic, array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
N = int(input())

xs = []
for _ in range(N):
    xs.append(input())
    
if all(x > y for x, y in zip(xs, xs[1:])):
    print("DECREASING")
elif all(x < y for x, y in zip(xs, xs[1:])):
    print("INCREASING")
else:
    print("NEITHER")