# Ordinals
# https://open.kattis.com/problems/ordinals
# TAGS: precompute, recursion
# CP4: 5.2a, Finding Formula, Easier
# NOTES:
VNO = [r"{}", r"{{}}"] # used r just in case there is weird f-string behavior using { and }, don't think it's needed

for i in range(2, 8 + 1):
    VNO.append("{" + ','.join(VNO[j] for j in range(i)) + '}')
    
n = int(input())

print(VNO[n])