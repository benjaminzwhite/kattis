# Pizzubestun
# https://open.kattis.com/problems/pizzubestun
# TAGS: array
# CP4: 3.4b, Involving Sorting, E
# NOTES:
n = int(input())

xs = []
for _ in range(n):
    _, price = input().split()
    xs.append(int(price))

xs = sorted(xs, reverse=True)
i = 0
res = 0
while i < n:
    res += xs[i]
    i += 2

print(res)