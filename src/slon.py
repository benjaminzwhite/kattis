# Slon
# https://open.kattis.com/problems/slon
# TAGS: mathematics, brute force
# CP4: 0, Not In List Yet
# NOTES:
"""
Obviously easy if you use Python eval()

Only tricky thing is to notice you only need to eval() the f(x) expression twice: e.g. once for x=0, once for x=1

Because then you can determine f(x) = ax + b for all values and you don't need repeated calls to eval(huge_expression.replace(x))
since it says expression can be of size 100_000 chars (so you would would time out if you eval it 10**6 times)
"""
s = input()

# says f(x) always deg=1: f(x) = ax + b
# f(x) = ax + b, evaluated at x=0, 1 gives:
# f(0) = b
# f(1) = a+b
b = eval(s.replace('x', '0'))
a = eval(s.replace('x', '1')) - b

# now you can brute force, without needing to call eval() 10**6 times
P, M = map(int, input().split())
for x in range(10 ** 6 + 1):
    if (a * x + b) % M == P:
        print(x)
        break