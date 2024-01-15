# No Duplicates
# https://open.kattis.com/problems/nodup
# TAGS: basic
# CP4: 2.3d, Hash Table (set)
# NOTES:
xs = input().split()

if len(xs) == len(set(xs)):
    print("yes")
else:
    print("no")