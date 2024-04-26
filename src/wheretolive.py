# Where to Live?
# https://open.kattis.com/problems/wheretolive
# TAGS: basic
# CP4: 9.grad, Gradient Descent
# NOTES:
"""
Don't know why it is 4+ difficulty O_o ?

CARE! I got a WA because Python rounds UP default behavior but the question wants rounded DOWN in case of a value having exactly .5 decimal

Also, implementation - don't need to create the xs/ys list, can just take running sum
"""
while True:
    n = int(input())
    if n == 0:
        break
    
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    xa = sum(xs) / len(xs)
    ya = sum(ys) / len(ys)

    rnd = lambda x: int(x) if x % 1 == 0.5 else round(x) # CARE! round down is asked for!
    print(rnd(xa), rnd(ya))