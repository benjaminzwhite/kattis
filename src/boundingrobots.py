# Bounding Robots
# https://open.kattis.com/problems/boundingrobots
# TAGS: interpreter, geometry
# CP4: 1.4i, Still Easy
# NOTES:
while True:
    w, l = map(int, input().split())
    if w == 0 and l == 0:
        break
    n = int(input())
    ax, ay, rx, ry = 0, 0, 0, 0 
    for _ in range(n):
        op, val = input().split()
        val = int(val)
        if op == 'r':
            rx += val
            ax = min(ax + val, w - 1)
        elif op =='l':
            rx -= val
            ax = max(ax - val, 0)
        elif op =='u':
            ry += val
            ay = min(ay + val, l - 1)
        else:
            ry -= val
            ay = max(ay - val, 0)
    print("Robot thinks", rx, ry)
    print("Actually at", ax, ay)
    print()