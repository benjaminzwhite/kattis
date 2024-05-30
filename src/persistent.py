# Persistent Numbers
# https://open.kattis.com/problems/persistent
# TAGS: mathematics, number theory, brute force
# CP4: 5.3h, Working with PFs
# NOTES:
"""
Just do trial division by 9,8,7....
"""
while True:
    n = int(input())
    if n == -1:
        break
        
    if n < 10:
        print(f"1{n}")
    else:
        res = []
        for d in range(9, 1, -1):
            while n % d == 0:
                res.append(d)
                n //= d
        if n > 1:
            print("There is no such number.")
        else:
            print(''.join(map(str, res[::-1])))