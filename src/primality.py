# Primality
# https://open.kattis.com/problems/primality
# TAGS: mathematics, number theory
# CP4: 0, Not In List Yet
# NOTES:
"""
- Input n is 10**18 so need fast primality check, it's a performance test basically.
- I used a not-very-optimized Miller Rabin with 15 rounds, passed first attempt.
- Reused some code that I've used elsewhere on other OJs O_o
"""
from random import randint

# reusing code
def miller_rabin(n, rounds):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n == 4:
        return False
    if n == 5:
        return True
    nn = n - 1
    exponent = 0
    while not (nn & 1):
        nn >>= 1
        exponent +=1
    # n = (2**exponent) * nn + 1
    for _ in range(rounds):
        flg = True
        rand_n = randint(2, n - 2)
        witness = pow(rand_n, nn, n)
        if witness == 1 or witness == n - 1:
            flg = False
            continue
        for _ in range(exponent - 1):
            witness = pow(witness, 2, n)
            if witness == n - 1:
                flg = False
                continue
        if flg:
            return False
    return True

n = int(input())

res = miller_rabin(n, 15)

if res:
    print("YES")
else:
    print("NO")