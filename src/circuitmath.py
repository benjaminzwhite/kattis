# Circuit Math
# https://open.kattis.com/problems/circuitmath
# TAGS: stack, interpreter
# CP4: 2.2k, Stack-based Problems
# NOTES:
N = int(input())

tf = []
for b in input().split():
    if b == "T":
        tf.append(True)
    else:
        tf.append(False)

stk = []
for c in input().split():
    if c.isalpha():
        stk.append(tf[ord(c) - ord("A")])
    else:
        if c == "*":
            b1 = stk.pop()
            b2 = stk.pop()
            res = b1 and b2
            stk.append(res)
        elif c == "+":
            b1 = stk.pop()
            b2 = stk.pop()
            res = b1 or b2
            stk.append(res)
        else:
            b1 = stk.pop()
            res = not b1
            stk.append(res)

res = stk.pop()
if res:
    print("T")
else:
    print("F")