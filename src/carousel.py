# Carousel
# https://open.kattis.com/problems/carousel
# TAGS: basic
# CP4: 1.4j, Medium
# NOTES:
"""
Confusing input - read carefully n,m and a,b.
"""
while True:
    n, m = map(int, input().split())
    if (n, m) == (0,0):
        break
    
    res_a, res_b = 1, 10**9
    for _ in range(n):
        a, b = map(int, input().split())
        if (a <= m) and ((res_b == 10**9) or (a * res_b > b * res_a) or (a * res_b == b * res_a and a > res_a)):
            res_a, res_b = a, b
    if (res_a, res_b) == (1, 10**9):
        print("No suitable tickets offered")
    else:
        print(f"Buy {res_a} tickets for ${res_b}")