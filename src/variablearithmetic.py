# Variable Arithmetic
# https://open.kattis.com/problems/variablearithmetic
# TAGS: interpreter
# CP4: 2.3e, Hash Table (map), E
# NOTES:
d = {}

while True:
    t = input().split()
    val = 0
    tmp = []
    if t[0] == '0':
        break
    if len(t) > 1 and t[1] == '=':
        d[t[0]] = int(t[2])
    else:
        for c in t:
            if c.isdigit():
                val += int(c)
            elif c in d:
                val += d[c]
            elif c != '+':
                tmp.append(c)
        if val > 0 or val == 0 and tmp == []:
            tmp.insert(0, val)
        print(' + '.join(map(str, tmp)))