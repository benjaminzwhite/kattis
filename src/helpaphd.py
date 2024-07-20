# Help a PhD candidate out!
# https://open.kattis.com/problems/helpaphd
# TAGS: basic
# CP4: 1.4d, Multiple TC + Selection
# NOTES:
"""
Was testing to see if eval() can be used on Kattis O_o
"""
N = int(input())

for _ in range(N):
    x = input()
    if x == 'P=NP':
        print('skipped')
    else:
        print(eval(x))