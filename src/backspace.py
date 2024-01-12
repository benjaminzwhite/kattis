# Backspace
# https://open.kattis.com/problems/backspace
# TAGS: stack
# CP4: 2.2l, List/Queue/Deque
# NOTES:
s = input()

stk = []

for c in s:
    if c == '<':
        stk.pop()
    else:
        stk.append(c)
        
print(''.join(stk))