# Another Brick in the Wall
# https://open.kattis.com/problems/anotherbrick
# TAGS: basic, array
# CP4: 1.4j, Medium
# NOTES:
h, w, n = map(int, input().split())
xs = map(int, input().split())

acc = 0
flg = True

for x in xs:
    acc += x
    if acc > w:
        flg = False
        break
    elif acc == w:
        acc = 0
        h -= 1
        if h == 0:
            break

if flg and h == 0:
    print("YES")
else:
    print("NO")