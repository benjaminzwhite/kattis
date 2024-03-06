# Math Homework
# https://open.kattis.com/problems/mathhomework
# TAGS: basic, mathematics, brute force
# CP4: 3.2c, Three+ Nested Loops, E
# NOTES:
"""
Brute force 3 ranges up to N doesnt work (takes 5-6 seconds) but only need to loop up to N//a for the a-multiplier coefficient, x
Same for N//b when looking for values of y etc. since at the end we want a*x + b*y + c*z == N so if a*x > N already it is impossible
"""
a, b, c, N = map(int, input().split())

res = []
for x in range(N // a + 1):
    for y in range(N // b + 1):
        for z in range(N // c + 1):
            if a * x + b * y + c * z == N:
                res.append((x, y, z))

if not res:
    print("impossible")
else:
    for l in res:
        print(*l)