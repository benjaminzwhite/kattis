# Cracking RSA
# https://open.kattis.com/problems/crackingrsa
# TAGS: brute force, mathematics, number theory
# CP4: 3.2i, Math Simulation, Harder
# NOTES:
T = int(input())

for _ in range(T):
    n, e = map(int, input().split())
    
    for f in range(2, int(n ** 0.5) + 1):
        if n % f == 0:
            p = f
            q = n // f
            break
    
    phi = (p - 1) * (q - 1)
    
    for d in range(1, phi + 1):
        if d * e % phi == 1:
            print(d)
            break