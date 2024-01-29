# Bracket Matching
# https://open.kattis.com/problems/bracketmatching
# TAGS: array, stack
# CP4: 2.2j, Stack
# NOTES:
"""
Classic stack problem - make sure to check that stack is empty at end of input
also: e.g. [()]{ is not valid even though the "stack part" of the code behaves OK
because there is an unpaired { on the stack at the end of the iteration. 
"""
PAIRS = {'(':')', '[':']', '{':'}'}

n = int(input())
s = input()

stk = []
flg = True
for c in s:
    if c in PAIRS:
        stk.append(c)
    else:
        if not stk or PAIRS[stk.pop()] != c:
            flg = False
            break

if (not stk) and flg:
    print("Valid")
else:
    print("Invalid")