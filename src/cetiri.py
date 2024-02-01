# Cetiri
# https://open.kattis.com/problems/cetiri
# TAGS: array
# CP4: 1.4g, 1D Array, Easier
# NOTES:
p, q, r = sorted(map(int, input().split()))

if r - q > q - p:
    print(2 * q - p)
elif r - q == q - p:
    print(2 * r - q)
elif r - q < q - p:
    print(p + r - q)