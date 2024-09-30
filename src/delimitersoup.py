# Delimiter Soup
# https://open.kattis.com/problems/delimitersoup
# TAGS: stack
# CP4: 2.2k, Stack-based Problems
# NOTES:
L = int(input())
s = input()

stk = []
REF = {')':'(', ']':'[', '}':'{'}

flg = True
for i, c in enumerate(s):
    if c in {'[', '(', '{'}:
        stk.append(c)
    elif c in REF:
        if not stk or (_ := stk.pop()) != REF[c]:
            print(f"{c} {i}")
            flg = False
            break

if flg:
    print("ok so far")