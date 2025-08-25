# Missing Gnomes
# https://open.kattis.com/problems/missinggnomes
# TAGS: set
# CP4: 2.3i, Balanced BST (set)
# NOTES:
n, m = map(int, input().split())

xs = []
for _ in range(m):
    xs.append(int(input()))

X = set(xs)
it = list(filter(lambda x: x not in X, range(1, n + 1)))

i = 0
for x in xs:
    while i < len(it) and it[i] < x: # CARE! check i < len(it) to avoid errors
        print(it[i])
        i += 1
    print(x)

# remaining elements
if i < len(it):
    for y in it[i:]:
        print(y)