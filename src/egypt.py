# Egypt
# https://open.kattis.com/problems/egypt
# TAGS: mathematics, geometry, basic
# CP4: 7.2d, Triangles (Trig)
# NOTES:
while True:
    a, b, c = sorted(map(int, input().split()))
    if (a, b, c) == (0, 0, 0):
        break
    
    if a * a + b * b == c * c:
        print("right")
    else:
        print("wrong")