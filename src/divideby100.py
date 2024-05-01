# Divide by 100...
# https://open.kattis.com/problems/divideby100
# TAGS: array, string
# CP4: 2.2b, 1D Array, Harder
# NOTES:
num = input()
den = input()

L = len(den)

num = num.zfill(L)

if L == 1:
    print(num)
else:
    res = num[:-L+1] + '.' + num[-L+1:]
    
    res = res.rstrip('0')

    if res.endswith('.'):
        print(res[:-1])
    elif res.startswith('.'):
        print('0' + res)
    else:
        print(res)