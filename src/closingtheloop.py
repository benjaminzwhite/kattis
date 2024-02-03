# Closing the Loop
# https://open.kattis.com/problems/closingtheloop
# TAGS: sorting
# CP4: 2.2e, Sorting, Easier
# NOTES:
N = int(input())

for case in range(1, N + 1):
    S = int(input()) # not needed for input in Python
    line = input()

    blue, red = [],[]

    for x in line.split():
        if x[-1] == 'B':
            blue.append(int(x[:-1]))
        else:
            red.append(int(x[:-1]))

    blue = sorted(blue, reverse=True)
    red = sorted(red, reverse=True)

    res = 0

    for i in range(min(len(blue), len(red))):
        res += blue[i]
        res += red[i]
        res -= 2

    print(f"Case #{case}: {res}")