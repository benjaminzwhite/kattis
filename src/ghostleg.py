# Ghost Leg
# https://open.kattis.com/problems/ghostleg
# TAGS: array
# CP4: 1.4i, Still Easy
# NOTES:
n, m = map(int, input().split())

xs = [int(input()) for _ in range(m)]

original = list(range(1, n+1))

for x in xs:
    original[x-1], original[x] = original[x], original[x-1]
    
for y in original:
    print(y)