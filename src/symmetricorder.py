# Symmetric Order
# https://open.kattis.com/problems/symmetricorder
# TAGS: array
# CP4: 2.2j, Stack
# NOTES:
t = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    names = [input() for _ in range(n)]
    print("SET", t)
    for x in names[::2]:
        print(x)
    for x in names[1::2][::-1]:
        print(x)
    t += 1