# Jumbled Compass
# https://open.kattis.com/problems/compass
# TAGS: basic
# CP4: 1.6e, Real Life, Easier
# NOTES:
s = int(input())
e = int(input())

option1 = (360 + e - s) % 360
option2 = (360 + e - s) % -360

if abs(option1) <= abs(option2):
    print(option1)
else:
    print(option2)