# Magic Trick
# https://open.kattis.com/problems/magictrick
# TAGS: basic
# CP4: 2.2e, Sorting, Easier
# NOTES:
s = input()

print(1 if len(s) == len(set(s)) else 0)