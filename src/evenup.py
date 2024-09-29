# Even Up Solitaire
# https://open.kattis.com/problems/evenup
# TAGS: stack
# CP4: 2.2j, Stack
# NOTES:
n = int(input())

xs = map(int, input().split())

stk = []
res = n

for x in xs:
    if not stk:
        stk.append(x)
        continue
    if (stk[-1] % 2) == (x % 2): # top of stack and current element x share parity -> so their sum is even, can remove this pair of elements
        stk.pop()
        res -= 2
    else:
        stk.append(x)
        
print(res)