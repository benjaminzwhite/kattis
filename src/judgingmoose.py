# Judging Moose
# https://open.kattis.com/problems/judgingmoose
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
l, r = map(int,input().split())

if l == 0 and r == 0:
    print("Not a moose")
elif l == r:
    print(f"Even {l + r}")
else:
    print(f"Odd {max(l, r) * 2}")