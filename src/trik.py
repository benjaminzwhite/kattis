# Trik
# https://open.kattis.com/problems/trik
# TAGS: basic
# CP4: 1.6c, Game (Others), Easier
# NOTES:
s = input()

l,m,r = 1,0,0

for c in s:
    if c == 'A':
        l,m = m,l
    elif c == 'B':
        m,r = r,m
    elif c == 'C':
        l,r = r,l

print(1*l + 2*m + 3*r)