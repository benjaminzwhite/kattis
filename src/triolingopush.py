# Triolingo Push
# https://open.kattis.com/problems/triolingopush
# TAGS: mathematics, recurrence
# CP4: 0, Not In List Yet
# NOTES:
"""
Reusing my simple Python implementation of matrix exponentiation I used elsewhere.

This exercise answer is "Fibonacci - 1".
(I just need to adjust n to n+1 for the initial conditions to line up with my implementation) 
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

n = int(input())
fib_rec = [[1, 1], [1, 0]]
BIGMOD = 10**9 + 7

res = matrix_bin_expon(fib_rec, n + 1, BIGMOD) # adjust n+1 for initial conditions to line up

print((res[0][0] - 1) % BIGMOD)