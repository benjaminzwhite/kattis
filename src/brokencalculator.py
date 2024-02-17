# Broken Calculator
# https://open.kattis.com/problems/brokencalculator
# TAGS: interpreter
# CP4: 1.4i, Still Easy
# NOTES:
n = int(input())

prev = 1

for _ in range(n):
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    
    if op == '+':
        prev = (a + b) - prev
    elif op == '-':
        prev = prev * (a - b)
    elif op == '*':
        prev = (a * b)**2
    else:
        prev = (a + 1) // 2
    
    print(prev)