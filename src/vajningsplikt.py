# Right-of-Way - Vajningsplikt
# https://open.kattis.com/problems/vajningsplikt
# TAGS: logic
# CP4: 1.4c, Selection Only
# NOTES:
DIRECTIONS = ["South", "East", "North", "West"] * 2
# Duplicate *2 the list of real directions to handle wraparound (i.e. index +1, +2, +3 etc. avoid index error)
# This is arranged in counterclockwise order so that increasing index means moving counterclockwise.

a, b, c = input().split()

ia = DIRECTIONS.index(a)

# condition 1:
if b == DIRECTIONS[ia + 2] and c == DIRECTIONS[ia + 1]:
    print("Yes")
# condition 2:
elif b == DIRECTIONS[ia + 3] and (c == DIRECTIONS[ia + 1] or c == DIRECTIONS[ia + 2]):
    print("Yes")
else:
    print("No")