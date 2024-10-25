# Lektira
# https://open.kattis.com/problems/lektira
# TAGS: array, brute force
# CP4: 3.2d, Three+ Nested Loops, H
# NOTES:
s = input()

res = s
l = len(s)

for i in range(1, l):
    for j in range(i + 1, l):
        a, b, c = s[:i], s[i:j], s[j:]
        tmp = a[::-1] + b[::-1] + c[::-1]
        if tmp < res:
            res = tmp

print(res)