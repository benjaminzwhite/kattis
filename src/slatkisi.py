# Slatkisi
# https://open.kattis.com/problems/slatkisi
# TAGS: basic
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
x, z = map(int, input().split())

if z == 0:
    print(x)
    
else:
    note = 10**z
    delta = x % note
    
    if delta >= note // 2:
        print(x + note - delta)
    else:
        print(x - delta)