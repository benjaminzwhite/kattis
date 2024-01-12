# Sort Two Numbers
# https://open.kattis.com/problems/sorttwonumbers
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
a, b = map(int, input().split())

print(min(a, b), max(a, b))