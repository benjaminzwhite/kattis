# Test Drive
# https://open.kattis.com/problems/testdrive
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
a, b, c = map(int, input().split())

if a < b > c or a > b < c:
    print("turned")
elif abs(b - a) < abs(c - b):
    print("accelerated")
elif abs(b - a) > abs(c - b):
    print("braked")
else:
    print("cruised")