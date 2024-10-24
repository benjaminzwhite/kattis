# Set!
# https://open.kattis.com/problems/set
# TAGS: array, brute force
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
inps = []

for _ in range(4):
    inps.extend(input().split())

flg = True

for i in range(12):
    for j in range(i + 1, 12):
        for k in range(j + 1, 12):
            a, b, c = inps[i], inps[j], inps[k]
            if all(len(set(col)) != 2 for col in zip(a, b, c)):
                print(i + 1, j + 1, k + 1)
                flg = False

if flg:
    print("no sets")