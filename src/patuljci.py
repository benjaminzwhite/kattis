# Patuljci
# https://open.kattis.com/problems/patuljci
# TAGS: brute force
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
xs = [int(input()) for _ in range(9)]

S = sum(xs)

for i in range(9):
    for j in range(i + 1, 9):
        if S - xs[i] - xs[j] == 100:
            avoids = [i, j]
            break

for i, x in enumerate(xs):
    if i not in avoids:
        print(x)