# Shopping List (Easy)
# https://open.kattis.com/problems/shoppinglisteasy
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
n, _ = map(int, input().split())

xs = set(input().split())

for _ in range(n - 1):
	xs = xs.intersection(set(input().split()))

print(len(xs))
for x in sorted(xs):
	print(x)