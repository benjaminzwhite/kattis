# Hot Hike
# https://open.kattis.com/problems/hothike
# TAGS: array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
n = int(input())

xs = list(map(int, input().split()))

day, max_res = -1, float('inf')

for i in range(len(xs) - 2):
    if (m := max(xs[i], xs[i+2])) < max_res:
        day = i + 1
        max_res = m

print(day, max_res)