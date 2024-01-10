# Cetvrta
# https://open.kattis.com/problems/cetvrta
# TAGS: basic
# CP4: 7.2f, Quadrilaterals
# NOTES:
from collections import defaultdict

d_x = defaultdict(int)
d_y = defaultdict(int)

for _ in range(3):
    x, y = input().split()
    d_x[x] += 1
    d_y[y] += 1
    
x_res = [x for x in d_x if d_x[x] == 1][0] 
y_res = [y for y in d_y if d_y[y] == 1][0]

print(f"{x_res} {y_res}")