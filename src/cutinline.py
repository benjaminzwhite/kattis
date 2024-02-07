# Cut in Line
# https://open.kattis.com/problems/cutinline
# TAGS: array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
N = int(input())

xs = []
for _ in range(N):
    xs.append(input())

C = int(input())

for _ in range(C):
    op, *v = input().split()
    if op == "cut":
        i = xs.index(v[1])
        xs.insert(i, v[0])
    else:
        xs.remove(v[0])

print(*xs, sep='\n')