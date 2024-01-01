# Quadrant Selection
# https://open.kattis.com/problems/quadrant
# TAGS: basic
# CP4: 1.4c, Selection Only
# NOTES:
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")
else:
    if y > 0:
        print("2")
    else:
        print("3")