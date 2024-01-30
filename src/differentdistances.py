# Different Distances
# https://open.kattis.com/problems/differentdistances
# TAGS: mathematics
# CP4: 5.2f, Log, Exp, Pow
# NOTES:
while True:
    l = input()
    if l == '0':
        break
    
    x, y, xx, yy, p = map(float, l.split())
    
    tmp = pow(abs(x - xx), p) + pow(abs(y - yy), p)
    print(pow(tmp, (1 / p)))