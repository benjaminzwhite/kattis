# Metaprogramming
# https://open.kattis.com/problems/metaprogramming
# TAGS: interpreter
# CP4: 2.3e, Hash Table (map), E
# NOTES:
from sys import stdin

d = {}

for line in stdin:
    command, *vals = line.split()
    if command == "define":
        v, k = vals
        d[k] = v
    elif command == "eval":
        a, op, b = vals
        if op == "=":
            op = "=="
        if a not in d or b not in d:
            print("undefined")
        else:
            res = eval(f"{d[a]} {op} {d[b]}")
            if res:
                print("true")
            else:
                print("false")