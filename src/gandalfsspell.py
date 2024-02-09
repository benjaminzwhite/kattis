# Gandalf's Spell
# https://open.kattis.com/problems/gandalfsspell
# TAGS: array
# CP4: 2.3e, Hash Table (map), E
# NOTES:
s = input()
t = input().split()

d = {}
e = {}
flg = True

for a, b in zip(s, t):
    if a in d and d[a] != b or b in e and e[b] != a:
        flg = False
        break
    else:
        d[a] = b
        e[b] = a

if flg and len(s) == len(t):
    print("True")
else:
    print("False")