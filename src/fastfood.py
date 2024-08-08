# Fast Food Prizes
# https://open.kattis.com/problems/fastfood
# TAGS: array, brute force
# CP4: 1.4j, Medium
# NOTES:
T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    to_process = []
    for _ in range(n):
        k, *vals, cash_value = map(int, input().split())
        to_process.append((vals, cash_value))
    
    stickers = list(map(int, input().split()))
    res = 0
    for vals, cash_value in to_process:
        cnt = min(x for i, x in enumerate(stickers, 1) if i in vals) # CARE! 1 based indexing for the result
        res += cnt * cash_value
        
    print(res)