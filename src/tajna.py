# Tajna
# https://open.kattis.com/problems/tajna
# TAGS: cipher, mathematics
# CP4: 1.6l, Cipher, Medium
# NOTES:
s = input()

L = len(s)

def get_r(l):
    for d in range(int(l ** 0.5), 0, -1):
        if l % d == 0:
            return d
            
R = get_r(L)
C = L // R

res = ''.join(s[r + c] for r in range(R) for c in range(0, R * C, R))

print(res)