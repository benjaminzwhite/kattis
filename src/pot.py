# Pot
# https://open.kattis.com/problems/pot
# TAGS: mathematics
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
N = int(input())

res = 0

for _ in range(N):
    x = input()
    res += int(x[:-1]) ** int(x[-1])
    
print(res)