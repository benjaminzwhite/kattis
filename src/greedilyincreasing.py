# Greedily Increasing Subsequence
# https://open.kattis.com/problems/greedilyincreasing
# TAGS: array
# CP4: 2.2a, 1D Array, Medium
# NOTES:
N = int(input())

xs = map(int, input().split())

prev = -1
res = []

for x in xs:
    if x > prev:
        res.append(str(x)) # convert to str!!
        prev = x

print(len(res))   
print(' '.join(res))