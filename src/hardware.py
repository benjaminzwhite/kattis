# Hardware
# https://open.kattis.com/problems/hardware
# TAGS: interpreter, dict
# CP4: 2.3c, DAT, Others
# NOTES:
"""
Reading comprehension:

You have to print digit vs digit**s** on the last output step, depending if it's 1 or more item (i.e remove/add 's' or not accordingly)
"""
T = int(input())

for _ in range(T):
    d = {k:0 for k in "0123456789"}

    name = input()
    hm_adresses = input()
    N, _ = hm_adresses.split()
    N = int(N)

    while N:
        line_tokens = input().split()
        if line_tokens[0] == '+':
            low, high, delta = map(int, line_tokens[1:])
            for n in range(low, high + delta, delta):
                N -= 1
                for digit in str(n):
                    d[digit] += 1
        else:
            N -= 1
            for digit in line_tokens[0]:
                d[digit] += 1

    print(name)
    print(hm_adresses)
    for k, v in d.items():
        print(f"Make {v} digit {k}")
    cnt = sum(v for v in d.values())
    if cnt > 1: # *sigh*
        print(f"In total {cnt} digits")
    else:
        print(f"In total {cnt} digit")