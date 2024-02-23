# 3D Printed Statues
# https://open.kattis.com/problems/3dprinter
# TAGS: mathematics
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
from math import ceil, log2

n = int(input())

res = 1 + ceil(log2(n))

print(res)