# Left Beehind
# https://open.kattis.com/problems/leftbeehind
# TAGS: basic
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    
    if (x + y) == 13:
        print("Never speak again.")
    elif x == y:
        print("Undecided.")
    elif x < y:
        print("Left beehind.")
    else:
        print("To the convention.")