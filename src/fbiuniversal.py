# FBI Universal Control Numbers
# https://open.kattis.com/problems/fbiuniversal
# TAGS: cipher, string
# CP4: 1.6e, Real Life, Easier
# NOTES:
"""
Do NOT include the check digit in the final calculation of the "score":

enumerate(s[:-1][::-1]) <--- note s[:-1] since you IGNORE the check_digit here
"""
ALPH = "0123456789ACDEFHJKLMNPRTVWX"
COEFFS = (2, 4, 5, 7, 8, 10, 11, 13)

T = int(input())

for _ in range(T):
    case_number, inp = input().split()

    d = {'B':'8', 'G':'C', 'I':'1', 'O':'0', 'Q':'0', 'S':'5', 'U':'V', 'Y':'V', 'Z':'2'}
    s = ''.join(d.get(c, c) for c in inp)

    check_digit = s[-1]

    check_sum = 0
    for coeff, d in zip(COEFFS, s[:-1]):
        check_sum += coeff * ALPH.index(d)

    if ALPH[check_sum % 27] == check_digit:
        res = 0
        for i, x in enumerate(s[:-1][::-1]):
            res += ALPH.index(x) * 27**i
        print(case_number, res)
    else:
        print(case_number, "Invalid")