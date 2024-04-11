# Select Group
# https://open.kattis.com/problems/selectgroup
# TAGS: interpreter, improve
# CP4: 6.2b, Input Parsing (Rec)
# NOTES:
"""
TODO: IMPROVE:

My implementation is to have a stack where either we have appended a string (which will correspond to the FIRST TIME WE SEE A NEW GROUP)
or a set, which is the current result of the set operations.

To check if we need to lookup a new set, I just do: if type(thing_popped_from_stack) == string

If so, then we need to lookup in groups{} dict for the actual set (this avoids creating multiple sets, not sure 
if there's a better way to do it / tradeoff for memory etc?)
"""
OPS = {"union":        lambda s, t: s.union(t),
       "intersection": lambda s, t: s.intersection(t),
       "difference":   lambda s, t: s - t}

groups = {}

while True:
    try:
        l = input().split()

        if l[0] == "group":
            _, name, _, *xs = l
            groups[name] = set(xs)
        else:
            tmp = l[::-1]
            stk = [groups[tmp[0]]]
            for x in tmp[1:]:
                if x in OPS:
                    left = stk.pop()
                    if type(left) == str:
                        left = groups[left]
                    right = stk.pop()
                    if type(right) == str:
                        right = groups[right]
                    res = OPS[x](left, right)
                    stk.append(res)
                else:
                    stk.append(x)
            print(*sorted(stk[0]))
    except EOFError:
        break