# Parket
# https://open.kattis.com/problems/parket
# TAGS: mathematics, number theory, logic
# CP4: 5.3h, Working with PFs
# NOTES:
"""
Reading comprehension:
Have to read description carefully to notice that the R bricks are all in a layer 1-brick thick around the boundary
Hence there are w+w+h+h+4 (R)ed bricks where w,h is the width,height of the inner (B)rown rectangle

CARE! also, wants a specific output requirement, hence the w < h check to print the min/max values correctly in the output
"""
R, B = map(int, input().split())

for d in range(1, int(B**0.5) + 1):
    if B % d == 0:
        h = B // d
        w = d
        if w + w + h + h + 4 == R: # +4 because of the 4 corner squares in the outermost layer 
            if w < h:
                w, h = h, w
            print(w + 2, h + 2)