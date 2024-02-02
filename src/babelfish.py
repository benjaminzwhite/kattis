# Babelfish
# https://open.kattis.com/problems/babelfish
# TAGS: basic
# CP4: 2.3e, Hash Table (map), E
# NOTES:
d = {}

while True:
    line = input()
    if line == "":
        break
    e, f = line.split()
    d[f] = e
    
while True:
    try:
        f = input()
        print(d.get(f, "eh"))
    except EOFError:
        break