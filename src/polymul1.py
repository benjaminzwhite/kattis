# Polynomial Multiplication 1
# https://open.kattis.com/problems/polymul1
# TAGS: basic, mathematics
# CP4: 5.2h, Polynomial
# NOTES:
T = int(input())

for _ in range(T):
    d1 = int(input())
    c1 = map(int, input().split())
    d2 = int(input())
    c2 = list(map(int, input().split()))
    # convert c2 to list since iterate over it multiple times
    
    coeffs_res = [0] * (d1 + d2 + 1)
    for i, x in enumerate(c1):
        for j, y in enumerate(c2):
            coeffs_res[i + j] += x * y
    
    print(d1 + d2)
    print(' '.join(map(str, coeffs_res)))