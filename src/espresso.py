# Espresso!
# https://open.kattis.com/problems/espresso
# TAGS: basic, logic
# CP4: 1.4h, Easy
# NOTES:
"""
Make sure you take t -= q when you refill since you still need to serve current customer when you trigger the "refill to s" step.
"""
n, s = map(int, input().split())

t = s
refills = 0

for _ in range(n):
    x = input()
    try:
        q = int(x)
    except:
        q = int(x[:-1]) + 1 # not very good practice O_o should parse q as string that may or may not end in 'L'
    if t - q >= 0:
        t -= q
    else:
        t = s
        t -= q # CARE! serve this customer after you refill to s 
        refills += 1

print(refills)