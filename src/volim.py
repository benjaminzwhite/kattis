# Volim
# https://open.kattis.com/problems/volim
# TAGS: basic
# CP4: 1.4h, Easy
# NOTES:
K = int(input())
N = int(input())

time = 0

while time < 210:
    t, z = input().split()
    t = int(t)
    time += t
    if time >= 210:
        print(K)
        break
    else:
        if z == 'T':
            K = 1 + (K % 8)