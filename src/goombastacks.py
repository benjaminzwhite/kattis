# Goomba Stacks
# https://open.kattis.com/problems/goombastacks
# TAGS: basic
# CP4: 1.4g, Control Flow, Level 1
# NOTES:
N = int(input())

acc = 0

flg = True
for _ in range(N):
    x, target = map(int, input().split())
    acc += x
    if acc < target:
        flg = False
        break
    
if flg:
    print("possible")
else:
    print("impossible")