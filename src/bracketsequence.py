# Bracket Sequence
# https://open.kattis.com/problems/bracketsequence
# TAGS: array, stack, interpreter, nice
# CP4: 2.2k, Stack-based Problems
# NOTES:
"""
Nice exercise.

The start operation is ADDITION, then when you encounter brackets you swap to MULT and back.

While coding I realised that could double-use the INDEX of the current operation i_op:
-> if i_op=0 corresponds to ADD,then can use that i_op (0) as the START_VALUE FOR ADDING TERMS (i.e. acc in functional programming)
-> similarly for i_op = 1 corresponding to MUL -> 1 is start value for a series of multiplications

---

Implementation notes:

Even with Python ints, need to take MOD during the calc steps to keep numbers manageable (else get TLE)
"""
from operator import add, mul

OPS = [add, mul] # i_op will be 0 for [add] and 1 for [mul]
EVAL_TOKEN = '#' # eval signal for stack
BIGMOD = 10**9 + 7

input() # not needed
s = input().split()

stk = []
i_op = 0 # start operation is addition

for x in s:
    if x == '(':
        # swap operation
        i_op = i_op ^ 1
        stk.append(EVAL_TOKEN)
    elif x == ')':
        tmp = i_op # since i_op is 0 for [add] and 1 for [mul] we can also use i_op as default value for ADDITION (0) and MULITPLICATION (1) (reduce with acc,x and initial value for acc = 0 or 1 respectively)
        while stk[-1] != EVAL_TOKEN:
            y = stk.pop()
            tmp = OPS[i_op](tmp, y) % BIGMOD
        stk.pop()
        stk.append(tmp)
        i_op = i_op ^ 1
    else:
        stk.append(int(x))

res = sum(stk) % BIGMOD # stack at the end contains only terms involving ADDITION operators so sum them all

print(res)