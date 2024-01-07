# Tarifa
# https://open.kattis.com/problems/tarifa
# TAGS: brute force
# CP4: 3.2g, Try All Answers
# NOTES:
L, H = map(int, input().split())

res = 0

for n in range(L, H+1):
    # all digits must be distinct, 0 not allowed in n either
    sn = str(n)
    if len(set(sn)) == 6 and '0' not in sn:
        if all(n % int(d) == 0 for d in sn):
            res += 1

print(res)