# Bit by Bit
# https://open.kattis.com/problems/bitbybit
# TAGS: interpreter
# CP4: 2.2h, Bit Manipulation
# NOTES:
while True:
    n = int(input())
    if n == 0:
        break
    
    register = ['?'] * 32 # should use -1 for not mixing data types
    
    for _ in range(n):
        op, *vals = input().split()
        vals = list(map(int, vals))
        b = vals[0] # the first (of 1, sometimes 2) value(s) is always the register that is updated
        if op == "CLEAR":
            register[b] = 0
        elif op == "SET":
            register[b] = 1
        elif op == "OR":
            if any(register[i] == 1 for i in vals):
                register[b] = 1
            elif all(register[i] == 0 for i in vals):
                register[b] = 0
            else:
                register[b] = '?'
        elif op == "AND":
            if all(register[i] == 1 for i in vals):
                register[b] = 1
            elif any(register[i] == 0 for i in vals): # deleted this by mistake on first submission hence W.A. on first try :/
                register[b] = 0
            else:
                register[b] = '?'
    
    print(''.join(map(str, register[::-1])))