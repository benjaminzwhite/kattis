# Another Candies
# https://open.kattis.com/problems/anothercandies
# TAGS: basic
# CP4: 5.3i, Modular Arithmetic
# NOTES:
"""
- Quite old exercise so difficulty is really over-ranked O_o, it's just taking a modulus
"""
T = int(input())

for _ in range(T):
    input()
    N = int(input())
    res = 0
    for _ in range(N):
        res += int(input())
    
    if res % N == 0:
        print("YES")
    else:
        print("NO")