# Inheritance
# https://open.kattis.com/problems/inheritance
# TAGS: stack, mathematics
# CP4: 0, Not In List Yet
# NOTES:
target = int(input())

res = []
stk = [2, 4]

while q:
    n = stk.pop()
    if n <= target:
        if target % n == 0:
            res.append(n)
        stk.append(10 * n + 2)
        stk.append(10 * n + 4)

for x in sorted(res):
	print(x)