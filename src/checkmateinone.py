# Checkmate in One
# https://open.kattis.com/problems/checkmateinone
# TAGS: grid, logic, nice
# CP4: 1.6b, Game (Chess)
# NOTES:
"""
Important:

The approach below works because we are guaranteed that no piece STARTS IN ATTACKED POSITION
e.g. R...k is not a valid input - because my approach returns FALSE/no checkmate for these cases.

---

Case analysis:

The only way you can put king in checkmate is if you have

K space ENEMY_KING | WALL and then if you can move rook to force check

-> So basically you want ENEMY KING on one of the 4 borders, and for rook to be able to place in check.
   THIS IS THE CASE IF ROOK IS NOT IN SAME "k,k-1,k+1" LINE.
   Since otherwise: 1) If in same k-line, its view is blocked by its own king.
                    2) If in +/-1 line, IT CAN BE TAKEN BY THE ENEMY KING WHEN IT TRIES TO PLACE IT IN CHECK
-> HOWEVER SOME EDGE CASES:
   When enemy king is in a CORNER then your king doesnt have to be on same row, it can be on +/-1 row/col depending on the geometry:

....k
..K..   instead of usual: ...K.k| pattern with k against single wall. This is because corner denies up_movement (down/keft/right depending on which corner ofc) 
.....

Also need to consider cases like this:

........
........
........
........
........
........
.R...K..
.......k

The above geometry ALLOWS FOR R TO MOVE TO THE SAME LINE AS ENEMY KING k. SO YOU NEED TO ADD:

if (ekr!=kr) or rookr not in {kr,kr-1,kr+1}: <--- check that ekr != kr enemy king row != king row; this handles the above cases

Same same for cols: if (ekc!=kc) or rookc not in {kc,kc-1,kc+1}:
"""
for r in range(8):
    for c, cell in enumerate(input().strip()):
        if cell == 'K':
            kr, kc = r, c
        elif cell == 'k':
            ekr, ekc = r, c
        elif cell == 'R':
            rookr, rookc = r, c

flg = False

if ((ekc == 0 and kc == 2) or (ekc == 7 and kc == 5)) and (ekr == kr or (ekr == 0 and kr == 1) or (ekr == 7 and kr == 6)):
    if (ekr != kr) or rookr not in {kr, kr - 1, kr + 1}:
        flg = True

if ((ekr == 0 and kr == 2) or (ekr == 7 and kr == 5)) and (ekc == kc or (ekc == 0 and kc == 1) or (ekc == 7 and kc == 6)):
    if (ekc != kc) or rookc not in {kc, kc - 1, kc + 1}:
        flg = True

if flg:
    print("Yes")
else:
    print("No")