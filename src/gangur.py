# Gangur
# https://open.kattis.com/problems/gangur
# TAGS: array, logic
# CP4: 3.5a, 1D Range Sum
# NOTES:
s = input()

acc = 0
res = 0
for c in s:
    if c == '>':
        acc += 1
    elif c == '<':
        res += acc

print(res)