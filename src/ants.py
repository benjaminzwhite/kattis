# Ants
# https://open.kattis.com/problems/ants
# TAGS: basic
# CP4: 3.4e, Non Classical, Easier
# NOTES:
"""
- CARE! main difficulty is understanding the weird input format. If you are given that there are n ants, these DO NOT appear all
  in one line e.g. 1 2 3 4 5 6 7 but rather can appear on multiple lines for some reason!?
  So you have to check, after each line, whether you have reached a total of n inputs (if not, you need to input the next line and repeat)
"""
T = int(input())

for _ in range(T):
    l, n = map(int, input().split())
    earliest, latest = -float('inf'), -float('inf')
    
    while n > 0: # weird input format - get e.g. 3 vals on line 1 then 4 vals on line 2 with n = 7 so need to track how many x's you have processed so far
        xs = map(int, input().split())
        for x in xs:
            n -= 1
            latest = max(latest, max(l - x, x))
            earliest = max(earliest, min(l - x, x))
    
    print(f"{earliest} {latest}")