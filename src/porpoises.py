# Immortal Porpoises
# https://open.kattis.com/problems/porpoises
# TAGS: mathematics, recurrence
# CP4: 5.8a, Matrix Power
# NOTES:
"""
It's "big fibonacci number" mod 10**9.

I hard coded 2x2 multiplication instead of NxN O_o
"""
def matrix_mult(a, b, modulus):
    mat_prod = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat_prod[i][j] += (a[i][k] * b[k][j]) % modulus
    return mat_prod

def matrix_bin_expon(a, n, modulus):
    mat_bin_exp = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            mat_bin_exp = matrix_mult(mat_bin_exp, a, modulus)
        a = matrix_mult(a, a, modulus)
        n = n // 2
    return mat_bin_exp

P = int(input())

for _ in range(P):
    k, n = map(int, input().split())
    fib_rec = [[1, 1], [1, 0]]
    BIGMOD = 10**9

    res = matrix_bin_expon(fib_rec, n, BIGMOD)

    print(k, res[0][1] % BIGMOD)