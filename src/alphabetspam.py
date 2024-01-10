# Alphabet Spam
# https://open.kattis.com/problems/alphabetspam
# TAGS: basic
# CP4: 2.3b, DAT, ASCII
# NOTES:
s = input()

a,b,c,d = 0,0,0,0

for char in s:
    if char == '_':
        a += 1
    elif char.islower():
        b += 1
    elif char.isupper():
        c += 1
    else:
        d += 1

l = len(s)

for x in (a,b,c,d):
    print(x/l)