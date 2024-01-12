# Linden Mayor System
# https://open.kattis.com/problems/lindenmayorsystem
# TAGS: string
# CP4: 6.2c, Regular Expression
# NOTES:
"""
Reading comprehension:

"Some letters may not have a rule associated with them. Such terminal letters are not replaced."

I thought this would mean replace such letters with ''

But it actually means replace such letter with THEMSELVES i.e. c -> c

"""
n, m = map(int, input().split())

d = {}
for _ in range(n):
    k, v = input().split(" -> ")
    d[k] = v
    
s = input()
for _ in range(m):
    s = ''.join(d.get(c, c) for c in s)
    
print(s)