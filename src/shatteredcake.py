# Shattered Cake
# https://open.kattis.com/problems/shatteredcake
# TAGS: basic
# CP4: 1.4j, Medium
# NOTES:
W = int(input())
N = int(input())
area = 0

for _ in range(N):
    w, l = map(int, input().split())
    area += w * l

print(area // W)